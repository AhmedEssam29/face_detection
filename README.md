Face Recognition & Anti-Spoofing System
This project is a face recognition and anti-spoofing system built using Tkinter, OpenCV, and face_recognition. The application features a user-friendly GUI to enable user login, logout, and registration using facial recognition, while also ensuring security through anti-spoofing techniques. It captures webcam images to recognize registered users and logs their activity, aiming to enhance secure access control.

Table of Contents
Features
Installation
Usage
Project Structure
Configuration
License
Features
User Authentication: Register, login, and logout functionalities with facial recognition.
Anti-Spoofing: Detects fake faces or spoofing attempts, improving security.
Image Logging: Logs user activity with timestamps to track attendance.
Tkinter GUI: A user-friendly interface to simplify interactions.
Installation
Prerequisites
Python 3.7+
Libraries:
face_recognition
opencv-python
Pillow
numpy
tkinter (usually included with Python)
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/face-recognition-anti-spoofing.git
cd face-recognition-anti-spoofing
Install the dependencies:

bash
pip install -r requirements.txt
Set up the model directory and database folder:
Set up the model directory and database folder:

Ensure the anti-spoofing models are in the specified path (default: resources/anti_spoof_models).
Create a db directory in the root folder to store user data.
Usage
To start the application, run:

bash
Copy code
python main.py
GUI Overview
Register New User: Opens a new window for face capture and user registration.
Login: Performs face recognition and anti-spoofing checks to allow access.
Logout: Logs the user out, capturing the timestamp of the exit.
Webcam Feed: Displays a live feed for capturing faces and checking liveness.
Registration Process
Click Register New User.
Input a username and capture the face.
If successful, the system saves the user's facial embedding.
Login Process
Click Login.
The system captures a frame, checks for liveness, and recognizes the face.
If successful, it welcomes the user and logs the entry.
Logout Process
Click Logout.
The system captures a frame, checks for liveness, and logs the exit time.
Project Structure
plaintext
Copy code
.
├── db/                         # Directory to store registered user data
├── resources/anti_spoof_models # Anti-spoofing models directory
├── main.py                     # Main application script
├── test.py                     # Anti-spoofing test script
├── util.py                     # Utility functions (button creation, message boxes)
├── log.txt                     # Log file for login/logout records
├── README.md                   # Project README file
└── requirements.txt            # Python dependencies
Configuration
Database Path: Ensure that self.db_dir in App.__init__ points to the correct directory for saving user data.
Anti-Spoofing Models Path: Set the correct path for the anti-spoofing models in test.py. This path can be configured via command-line arguments or by editing the script directly.
License
This project is licensed under the MIT License. See the LICENSE file for details.
