import cv2
import os
import pandas as pd
from deepface import DeepFace
from datetime import datetime

# Folder containing student images
DATABASE_PATH = "images"

# Attendance folder
ATTENDANCE_FOLDER = "Attendance"
os.makedirs(ATTENDANCE_FOLDER, exist_ok=True)

# Attendance file
current_date = datetime.now().strftime("%Y-%m-%d")
attendance_file = f"{ATTENDANCE_FOLDER}/Attendance_{current_date}.csv"

# Create CSV if not exists
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_csv(attendance_file, index=False)

# Load existing attendance
attendance_df = pd.read_csv(attendance_file)

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera could not be opened")
    exit()

print("AI Attendance System Started")
print("Press Q to Exit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    try:
        # Analyze face
        result = DeepFace.find(
            img_path=frame,
            db_path=DATABASE_PATH,
            enforce_detection=False,
            silent=True
        )

        # If face matched
        if len(result) > 0 and len(result[0]) > 0:
            matched_path = result[0].iloc[0]['identity']

            # Extract name from file
            name = os.path.basename(matched_path).split('.')[0]
            name = name.upper()

            # Check if already marked
            if name not in attendance_df['Name'].values:
                current_time = datetime.now().strftime("%H:%M:%S")

                new_entry = pd.DataFrame({
                    'Name': [name],
                    'Time': [current_time]
                })

                attendance_df = pd.concat([attendance_df, new_entry], ignore_index=True)
                attendance_df.to_csv(attendance_file, index=False)

                print(f"Attendance Marked for {name}")

            # Display name on screen
            cv2.putText(frame, name, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    except Exception as e:
        print("Face not detected")

    # Show webcam
    cv2.imshow("AI Attendance System", frame)

    # Exit on Q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()