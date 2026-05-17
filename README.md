# AI Attendance System

An AI-powered Attendance Management System using Face Recognition, OpenCV, and Python.

This project detects and recognizes faces in real-time through a webcam and automatically marks attendance in a CSV file.

---

## Features

- Real-time face recognition
- Automatic attendance marking
- CSV-based attendance storage
- Multiple student recognition
- Webcam integration using OpenCV
- Easy to use and beginner-friendly

---

## Technologies Used

- Python
- OpenCV
- DeepFace
- Pandas
- NumPy

---

## Project Structure

```bash
AI_Attendance_System/
│
├── main.py
├── images/
│   ├── Irene.jpg
│   ├── Rahul.jpg
│   └── Amal.jpg
│
├── Attendance/
│
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI_Attendance_System.git
cd AI_Attendance_System
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install opencv-python
pip install pandas
pip install deepface
pip install tf-keras
```

If TensorFlow causes issues:

```bash
pip install tensorflow==2.15.0
```

---

## Add Student Images

Place clear front-face images inside the `images` folder.

Example:

```bash
images/Irene.jpg
images/Rahul.jpg
```

The filename becomes the attendance name automatically.

---

## Run Project

```bash
python main.py
```

Press `Q` to exit the webcam window.

---

## Attendance Output

Attendance is automatically stored inside:

```bash
Attendance/
```

Example CSV:

```csv
Name,Time
IRENE,10:15:22
RAHUL,10:17:05
```

---

## Future Improvements

- GUI Interface
- SQLite Database
- Excel Export
- Unknown Face Detection
- Anti-Spoof Detection
- Cloud Database Integration
- Mobile Camera Support

---

## Author

Developed by Hida and Ridha
