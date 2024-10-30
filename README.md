# Face Recognition and Anti-Spoofing System

This project is a face recognition and anti-spoofing system built with Python, Tkinter, and OpenCV. It allows for secure and authenticated access via real-time face recognition, with liveness detection to prevent spoofing attempts. Users can log in, log out, and register new accounts. 

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Project Structure](#project-structure)
4. [Setup](#setup)
5. [Usage](#usage)
6. [How It Works](#how-it-works)
7. [Future Improvements](#future-improvements)

---

## Features

- **Login and Logout**: Authenticate users by recognizing their face and verifying their liveness to prevent unauthorized access.
- **Anti-Spoofing**: Detect spoofing attempts with a liveness detection model to ensure only live faces are authenticated.
- **User Registration**: Register new users with their facial encodings for future recognition.
- **Real-time Webcam Feed**: Display a live webcam feed within the Tkinter GUI.

---

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- OpenCV
- face_recognition
- PIL (Pillow)
- Tkinter
- NumPy

You can install the required packages by running:

```bash
pip install opencv-python-headless face_recognition pillow numpy

face_recognition_system/
│
├── main.py                  # Main application file (Tkinter GUI)
├── test.py                  # Anti-spoofing test script
├── util.py                  # Utility functions for GUI elements
├── src/
│   ├── anti_spoof_predict.py     # Anti-spoofing model class
│   ├── generate_patches.py       # Image processing and cropping
│   └── utility.py                # Model parsing and utilities
├── db/                     # User face encoding database
├── resources/
│   └── anti_spoof_models/       # Folder for anti-spoofing models
└── README.md               # Project README file
```
## Setup

#### 1.Clone the Repository

```bash
git clone https://github.com/username/face_recognition_system.git
cd face_recognition_system
```
#### 2.Download Anti-Spoofing Models

Place your anti-spoofing models in the resources/anti_spoof_models directory. You can download pre-trained models suitable for real-time face anti-spoofing from trusted sources.

#### 3.Run the Application

You can start the application by running:

```bash
python main.py
```


## Usage
#### Login

Click the Login button to authenticate. If a recognized user is detected, they will be logged in with a timestamp. If the face is not recognized or liveness is not confirmed, the user will be denied access.

#### Logout

Click the Logout button to log out the current user.

#### Register New User

Click the Register New User button to capture a face and register a new user by entering a username.

## How It Works
#### 1. Face Detection and Recognition
The system captures images from the webcam and converts them into facial embeddings using face_recognition.
It checks the database of registered faces in the db/ folder to find a match for the detected face.
#### 2. Anti-Spoofing Check
Before authenticating a user, the system runs an anti-spoofing check using test.py. This script uses the anti-spoofing model in src/anti_spoof_predict.py to detect if the face is live.
#### 3. User Registration
New users are registered by capturing a face image, encoding the face, and saving it as a .pickle file in the db/ directory for future recognition.


