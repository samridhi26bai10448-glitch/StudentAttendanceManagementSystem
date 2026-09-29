from validation import get_valid_classes


def calculate_attendance():
    total_classes, attended_classes = get_valid_classes()

    attendance_percentage = (attended_classes / total_classes) * 100

    print("\n--- Attendance Calculator ---")
    print(f"Total Classes: {int(total_classes)}")
    print(f"Classes Attended: {int(attended_classes)}")
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    return total_classes, attended_classes, attendance_percentage