import validation


def calculate_required_classes():
    print("\n--- Required Classes Calculator ---")

    total_classes, attended_classes = validation.get_valid_classes()
    target_percentage = validation.get_valid_target()

    current_percentage = (attended_classes / total_classes) * 100

    if current_percentage >= target_percentage:
        print(f"Current Attendance: {current_percentage:.2f}%")
        print("Target attendance has already been achieved.")
        return 0

    # A target of 100% cannot be reached if any class has already been missed.
    if target_percentage == 100:
        print(f"Current Attendance: {current_percentage:.2f}%")
        print("A 100% target cannot be reached because classes have already been missed.")
        return None

    required_classes = 0

    while True:
        required_classes += 1

        new_percentage = (
            (attended_classes + required_classes)
            / (total_classes + required_classes)
        ) * 100

        if new_percentage >= target_percentage:
            break

    print(f"Current Attendance: {current_percentage:.2f}%")
    print(f"Target Attendance: {target_percentage:.2f}%")
    print(f"Required Upcoming Classes: {required_classes}")

    return required_classes