import cv2
import os
import pandas as pd
from deepface import DeepFace
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Database path
DATABASE_PATH = "images"

# Attendance folder
ATTENDANCE_FOLDER = "Attendance"
os.makedirs(ATTENDANCE_FOLDER, exist_ok=True)

# Create attendance file
current_date = datetime.now().strftime("%Y-%m-%d")
attendance_file = f"{ATTENDANCE_FOLDER}/Attendance_{current_date}.csv"

if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_csv(attendance_file, index=False)

# Start Attendance Function
def start_attendance():

    attendance_df = pd.read_csv(attendance_file)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        messagebox.showerror("Error", "Camera could not be opened")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        try:
            result = DeepFace.find(
                img_path=frame,
                db_path=DATABASE_PATH,
                enforce_detection=False,
                silent=True
            )

            if len(result) > 0 and len(result[0]) > 0:
                matched_path = result[0].iloc[0]['identity']

                name = os.path.basename(matched_path).split('.')[0]
                name = name.upper()

                if name not in attendance_df['Name'].values:
                    current_time = datetime.now().strftime("%H:%M:%S")

                    new_entry = pd.DataFrame({
                        'Name': [name],
                        'Time': [current_time]
                    })

                    attendance_df = pd.concat([attendance_df, new_entry], ignore_index=True)
                    attendance_df.to_csv(attendance_file, index=False)

                    print(f"Attendance Marked for {name}")

                cv2.putText(frame, name, (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

        except Exception:
            pass

        cv2.imshow("AI Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Exit Function
def exit_app():
    root.destroy()

# GUI Window
root = tk.Tk()
root.title("AI Attendance System")
root.geometry("500x350")
root.configure(bg="#1e1e1e")

# Title
label = tk.Label(
    root,
    text="AI ATTENDANCE SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)
label.pack(pady=30)

# Start Button
start_btn = tk.Button(
    root,
    text="Start Attendance",
    command=start_attendance,
    font=("Arial", 14),
    bg="green",
    fg="white",
    width=20,
    height=2
)
start_btn.pack(pady=20)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    command=exit_app,
    font=("Arial", 14),
    bg="red",
    fg="white",
    width=20,
    height=2
)
exit_btn.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Powered by Python + DeepFace",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="lightgray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()