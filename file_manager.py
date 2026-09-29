import os


FILE_PATH = "data/attendance_records.txt"


def save_record(total_classes, attended_classes, attendance_percentage, status):
    try:
        os.makedirs("data", exist_ok=True)

        with open(FILE_PATH, "a") as file:
            file.write("----- Attendance Record -----\n")
            file.write(f"Total Classes: {int(total_classes)}\n")
            file.write(f"Classes Attended: {int(attended_classes)}\n")
            file.write(f"Attendance Percentage: {attendance_percentage:.2f}%\n")
            file.write(f"Attendance Status: {status}\n")
            file.write("----------------------------\n\n")

        print("\nAttendance record saved successfully.")

    except OSError:
        print("\nError: Unable to save the attendance record.")