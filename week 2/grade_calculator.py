
## 🧠 grade_calculator.py
def calculate_grade(marks):
    """
    This function takes marks as input and returns grade and message
    """
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better 😊"
    elif 60 <= marks <= 69:
        return "D", "Fair performance. Keep practicing 💪"
    else:
        return "F", "Don't give up! Learn and try again 🚀"


def get_valid_marks():
    """
    This function keeps asking for marks until valid input is entered
    """
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    print("📘 STUDENT GRADE CALCULATOR")
    print("-" * 30)

    student_name = input("Enter student name: ")

    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", student_name.upper())
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()
