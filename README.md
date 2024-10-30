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
bash```


