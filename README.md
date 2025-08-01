# 📷 Attendance System Using Facial Recognition

This project is a Python-based real-time attendance system using facial recognition. It uses the webcam to detect and recognize faces, marks attendance for recognized individuals, and saves the records in a `.csv` file with the current date.

---

## 🗂️ Project File

- `main.py` — The main Python script that performs real-time face recognition and logs attendance.
- `faces/` — Folder containing the images of known individuals (e.g., `tony_stark.jpg`, `steve_rogers.jpg`, `nikshay.jpg`).

---

## 🚀 Features

- Detects and recognizes faces using webcam
- Records attendance with name and timestamp
- Creates a dated `.csv` file for each session
- Supports multiple known individuals
- Real-time feedback by displaying name and status on the video feed

---

## 🔧 Requirements

Install the necessary Python libraries before running the script:

```bash
pip install cmake
pip install opencv-python
pip install face_recognition
pip install numpy
```

---

## ▶️ How to Run

1. Place images of known faces inside a folder named `faces/`.
   - Example: `faces/tony_stark.jpg`, `faces/steve_rogers.jpg`, `faces/nikshay.jpg`
2. Make sure the filenames and variable names match inside `main.py`.
3. Run the script:

```bash
python main.py
```

4. The webcam will open and start detecting faces.
5. Press `q` to stop the attendance session and close the window.

---

## 📝 Output

- A `.csv` file will be created with the current date as the filename (e.g., `30-07-2025.csv`)
- Format inside the CSV:

```
Name, Time
Tony, 10-12-01
Steve, 10-14-35

```

---

## 🧠 Concepts Used

- OpenCV for webcam handling and image processing
- `face_recognition` for face encoding, comparison, and recognition
- CSV file handling using Python's built-in `csv` module
- Datetime for timestamps and naming attendance files

---

## 📌 Notes

- `cv2.VideoCapture(0)` uses the default webcam. Change the index to `1`, `2`, etc., if using external cameras.
- Make sure lighting is good for better face detection.
- Images should be clear frontal photos of individuals for accurate encoding.

---
