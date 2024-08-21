import os
import datetime
import pickle
import streamlit as st
import cv2
import face_recognition
import numpy as np
from test import test

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

# Streamlit app
st.title("Face Recognition App")

mode = st.selectbox("Choose an option", ["Login", "Logout", "Register New User"])

if st.button("Capture Image"):
    img_np = capture_image()
    st.image(cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB), caption='Captured Image', use_column_width=True)

    if mode == "Login":
        label = test(
            image=img_np,
            model_dir='E:/face/face-attendance-system/resources/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            name = recognize(img_np, db_dir)
            if name == 'no_persons_found':
                st.error("No face detected. Please try again.")
            elif name == 'unknown_person':
                st.error("Unknown user. Please register a new user or try again.")
            else:
                with open(log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},in\n')
                st.success(f"Welcome back, {name}.")
        else:
            st.error("Wrong, you are fake!")

    elif mode == "Logout":
        label = test(
            image=img_np,
            model_dir='E:/face/face-attendance-system/resources/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            name = recognize(img_np, db_dir)
            if name == 'no_persons_found':
                st.error("No face detected. Please try again.")
            elif name == 'unknown_person':
                st.error("Unknown user. Please register a new user or try again.")
            else:
                with open(log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},out\n')
                st.success(f"Goodbye, {name}.")
        else:
            st.error("Wrong, you are fake!")

    elif mode == "Register New User":
        name = st.text_input("Enter a username")
        if name:
            embeddings = face_recognition.face_encodings(img_np)
            if not embeddings:
                st.error("No face found in the image.")
            else:
                file_path = os.path.join(db_dir, f'{name}.pickle')
                with open(file_path, 'wb') as file:
                    pickle.dump(embeddings[0], file)
                st.success("User was registered successfully!")
        else:
            st.error("Please enter a username.")
