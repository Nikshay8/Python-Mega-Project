# pip install cmake
# pip install opencv-python
# pip install face_recognition
# pip install numpy

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)           # 0, 1, 2, 3 depends on the web cam no. you are using on your computer

# Load Known Faces
tonys_image = face_recognition.load_image_file("faces/tony_stark.jpg")
tony_encoding = face_recognition.face_encodings(tonys_image)[0]

steves_image = face_recognition.load_image_file("faces/steve_rogers.jpg")
steve_encoding = face_recognition.face_encodings(steves_image)[0]

nikshays_image = face_recognition.load_image_file("faces/nikshay.jpg")
nikshay_encoding = face_recognition.face_encodings(nikshays_image)[0]


known_face_encodings = [tony_encoding, steve_encoding, nikshay_encoding]
known_face_names = ["Tony", "Steve", "Nikshay"]

#list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")            # Date-Month-Year

f = open(f"{current_date}.csv", "w+", newline = "")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()                # _, is written because the first argument for video_capture.read() is whether your video capture is successful or not & second argument is frame so frame is written afterwards
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)                   # fx and fy are the size by which we wanna resize
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)              # cvtColor means convert to color

    # Recognize Faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

        # Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerofText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + "Present", bottomLeftCornerofText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):          # means whenever we press 'q' button on keyboard we want the while loop to break
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()






