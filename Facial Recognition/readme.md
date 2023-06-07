# Attendance System with Face Recognition

This code is an implementation of an attendance system using face recognition. It captures video from a webcam, recognizes faces, and keeps track of the attendance of known individuals.

## Prerequisites

Before running the code, make sure you have the following:

1. Python: Ensure that you have Python installed on your system.
2. OpenCV: Install the OpenCV library to work with images and video.
3. face_recognition: Install the face_recognition library for face detection and recognition.
4. CSV: Make sure the `csv` module is available to handle reading and writing CSV files.

## Code Description

The code consists of the following steps:

1. Importing required libraries: The necessary libraries are imported, including `cv2`, `csv`, `numpy`, `face_recognition`, and `datetime`.
2. Setting up video capture: The code initializes the video capture using the default webcam (index 0).
3. Loading known faces: Known faces are loaded from image files using `face_recognition.load_image_file()` and encoded using `face_recognition.face_encodings()`.
4. Setting up variables: Variables for face locations, face encodings, and expected students are initialized.
5. Creating a CSV file: A CSV file is created with the current date as the filename.
6. Main loop: The code enters an infinite loop to continuously process video frames from the webcam.
   - The loop reads a frame from the video capture.
   - The frame is resized and converted to RGB format.
   - Faces are recognized in the frame using `face_recognition.face_locations()` and `face_recognition.face_encodings()`.
   - For each recognized face:
     - The code compares the face encoding with the known face encodings using `face_recognition.compare_faces()`.
     - The closest match is determined using `np.argmin()`.
     - If a match is found, the name of the person is identified.
     - If the person is in the list of expected students, their name and current time are recorded in the CSV file.
     - The person's name is displayed on the frame using `cv2.putText()`.
   - The frame is displayed with the attendance information.
   - The loop breaks if the 'q' key is pressed.
7. Cleanup: The video capture is released, and the CSV file is closed.
8. End of the code.

Please make sure to provide the necessary image files and create a folder named "Faces" in the same directory as the script. Place the known faces' images in the "Faces" folder with appropriate filenames and extensions

You can modify the code as per your requirements, such as adding more known faces or customizing the display text and formatting.

**Note:** Remember to install the required libraries and modules before running the code.