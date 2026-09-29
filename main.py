from attendance_calculator import calculate_attendance
from attendance_analyzer import analyze_attendance
from required_classes import calculate_required_classes
from file_manager import save_record


def display_menu():
    print("\n========================================")
    print(" STUDENT ATTENDANCE MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Calculate Attendance")
    print("2. Analyze Attendance")
    print("3. Calculate Required Classes")
    print("4. Save Attendance Record")
    print("5. Exit")
    print("========================================")


def main():
    last_total_classes = None
    last_attended_classes = None
    last_attendance_percentage = None
    last_status = None

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            (
                last_total_classes,
                last_attended_classes,
                last_attendance_percentage
            ) = calculate_attendance()

        elif choice == "2":
            if last_attendance_percentage is None:
                print("\nPlease calculate your attendance first.")
            else:
                last_status, advice = analyze_attendance(
                    last_attendance_percentage
                )

        elif choice == "3":
            calculate_required_classes()

        elif choice == "4":
            if last_attendance_percentage is None:
                print("\nPlease calculate your attendance first.")
            else:
                if last_status is None:
                    last_status, advice = analyze_attendance(
                        last_attendance_percentage
                    )

                save_record(
                    last_total_classes,
                    last_attended_classes,
                    last_attendance_percentage,
                    last_status
                )

        elif choice == "5":
            print(
                "\nThank you for using the Student Attendance Management System!"
            )
            print("Program ended.")
            break

        else:
            print(
                "\nError: Invalid choice. "
                "Please select a number from 1 to 5."
            )


if __name__ == "__main__":
    main() 