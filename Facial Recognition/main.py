import cv2
import csv
import numpy as np
import face_recognition
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load known faces
image1 = face_recognition.load_image_file('') # Enter path for the image file
image1_encoding = face_recognition.face_encodings(image1)[0]
image2 = face_recognition.load_image_file('') # Enter path for the image file
image2_encoding = face_recognition.face_encodings(image2)[0]

known_face_encodings = [image1_encoding, image2_encoding]
known_face_names = ["", ""] # Enter name you want to display for the face

# List of person
persons = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer()

while True:
    _, frame = video_capture.read()
    smallframe = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(smallframe, cv2.COLOR_BGR2RGB)
    
    # Recognise faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)
        
        if (matches[best_match_index]):
            name = known_face_names[best_match_index]
            
        # Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
            
            if name in persons:
                persons.remove(name)
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow(name, current_time)
                
            cv2.imshow("Attendance", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    video_capture.release()
    cv2.destroyAllWindows()
    f.close()