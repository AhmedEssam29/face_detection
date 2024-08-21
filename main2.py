import os
import datetime
import pickle
import cv2
import face_recognition
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from test import test

app = FastAPI()

# Set up directories
db_dir = './db'
if not os.path.exists(db_dir):
    os.mkdir(db_dir)

log_path = './log.txt'

def recognize(img_np, db_dir):
    encodings = face_recognition.face_encodings(img_np)
    
    if not encodings:
        return 'no_persons_found'

    embeddings = encodings[0]

    for filename in os.listdir(db_dir):
        with open(os.path.join(db_dir, filename), 'rb') as file:
            known_embedding = pickle.load(file)
            matches = face_recognition.compare_faces([known_embedding], embeddings)
            if matches[0]:
                return filename.split('.')[0]
    
    return 'unknown_person'

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

class UserRequest(BaseModel):
    mode: str
    username: str = None

@app.post("/face_recognition/")
def face_recognition_endpoint(request: UserRequest):
    # Capture an image from the webcam
    img_np = capture_image()

    if request.mode == "Login":
        label = test(
            image=img_np,
            model_dir='E:/face/face-attendance-system/resources/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            name = recognize(img_np, db_dir)
            if name == 'no_persons_found':
                raise HTTPException(status_code=400, detail="No face detected. Please try again.")
            elif name == 'unknown_person':
                raise HTTPException(status_code=400, detail="Unknown user. Please register a new user or try again.")
            else:
                with open(log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},in\n')
                return {"message": f"Welcome back, {name}."}
        else:
            raise HTTPException(status_code=400, detail="Wrong, you are fake!")

    elif request.mode == "Logout":
        label = test(
            image=img_np,
            model_dir='E:/face/face-attendance-system/resources/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            name = recognize(img_np, db_dir)
            if name == 'no_persons_found':
                raise HTTPException(status_code=400, detail="No face detected. Please try again.")
            elif name == 'unknown_person':
                raise HTTPException(status_code=400, detail="Unknown user. Please register a new user or try again.")
            else:
                with open(log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},out\n')
                return {"message": f"Goodbye, {name}."}
        else:
            raise HTTPException(status_code=400, detail="Wrong, you are fake!")

    elif request.mode == "Register New User":
        if request.username is None:
            raise HTTPException(status_code=400, detail="Username is required for registration.")

        embeddings = face_recognition.face_encodings(img_np)
        if not embeddings:
            raise HTTPException(status_code=400, detail="No face found in the image.")
        else:
            file_path = os.path.join(db_dir, f'{request.username}.pickle')
            with open(file_path, 'wb') as file:
                pickle.dump(embeddings[0], file)
            return {"message": "User was registered successfully!"}

    else:
        raise HTTPException(status_code=400, detail="Invalid mode. Please choose 'Login', 'Logout', or 'Register New User'.")
