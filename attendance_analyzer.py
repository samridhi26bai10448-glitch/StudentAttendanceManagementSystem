def analyze_attendance(attendance_percentage):
    print("\n--- Attendance Analyzer ---")

    if attendance_percentage >= 90:
        status = "Excellent"
        advice = "Your attendance is excellent. Continue maintaining regular attendance."

    elif attendance_percentage >= 75:
        status = "Good"
        advice = "Your attendance is good. Try to attend classes regularly to maintain it."

    elif attendance_percentage >= 65:
        status = "Warning"
        advice = "Your attendance needs attention. Try to attend upcoming classes regularly."

    else:
        status = "Critical"
        advice = "Your attendance is critically low. Attend upcoming classes regularly and monitor your attendance."

    print(f"Attendance Percentage: {attendance_percentage:.2f}%")
    print(f"Attendance Status: {status}")
    print(f"Advice: {advice}")

    return status, advice
