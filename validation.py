def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
            else:
                return value

        except ValueError:
            print("Error: Please enter a valid number.")


def get_valid_classes():
    while True:
        total_classes = get_valid_number("Enter total classes conducted: ")
        attended_classes = get_valid_number("Enter classes attended: ")

        if total_classes == 0:
            print("Error: Total classes must be greater than 0.")
        elif attended_classes > total_classes:
            print("Error: Attended classes cannot be greater than total classes.")
        else:
            return total_classes, attended_classes


def get_valid_target():
    while True:
        target = get_valid_number("Enter target attendance percentage: ")

        if target <= 0 or target > 100:
            print("Error: Target percentage must be between 0 and 100.")
        else:
            return target


def get_valid_attendance_percentage():
    while True:
        percentage = get_valid_number("Enter attendance percentage: ")

        if percentage > 100:
            print("Error: Attendance percentage cannot be greater than 100.")
        else:
            return percentage