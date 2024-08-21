import os
import datetime
import pickle
import cv2
import face_recognition
from flask import Flask, request, jsonify
from test import test

app = Flask(__name__)

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

@app.route("/face_recognition/", methods=["POST"])
def face_recognition_endpoint():
    data = request.json
    mode = data.get('mode')
    username = data.get('username', None)

    # Capture an image from the webcam
    img_np = capture_image()

    if mode == "Login":
        label = test(
            image=img_np,
            model_dir='E:/face/face-attendance-system/resources/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            name = recognize(img_np, db_dir)
            if name == 'no_persons_found':
                return jsonify({"detail": "No face detected. Please try again."}), 400
            elif name == 'unknown_person':
                return jsonify({"detail": "Unknown user. Please register a new user or try again."}), 400
            else:
                with open(log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},in\n')
                return jsonify({"message": f"Welcome back, {name}."})
        else:
            return jsonify({"detail": "Wrong, you are fake!"}), 400

    elif mode == "Logout":
        label = test(
            image=img_np,
            model_dir='E:/face/face-attendance-system/resources/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            name = recognize(img_np, db_dir)
            if name == 'no_persons_found':
                return jsonify({"detail": "No face detected. Please try again."}), 400
            elif name == 'unknown_person':
                return jsonify({"detail": "Unknown user. Please register a new user or try again."}), 400
            else:
                with open(log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},out\n')
                return jsonify({"message": f"Goodbye, {name}."})
        else:
            return jsonify({"detail": "Wrong, you are fake!"}), 400

    elif mode == "Register New User":
        if not username:
            return jsonify({"detail": "Username is required for registration."}), 400

        embeddings = face_recognition.face_encodings(img_np)
        if not embeddings:
            return jsonify({"detail": "No face found in the image."}), 400
        else:
            file_path = os.path.join(db_dir, f'{username}.pickle')
            with open(file_path, 'wb') as file:
                pickle.dump(embeddings[0], file)
            return jsonify({"message": "User was registered successfully!"})

    else:
        return jsonify({"detail": "Invalid mode. Please choose 'Login', 'Logout', or 'Register New User'."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
