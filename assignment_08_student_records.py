# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def show_menu():
    print()
    print("=" * 32)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 32)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def average(scores):
    total = 0
    for score in scores:
        total = total + score
    return round(total / len(scores), 2)


def scores_as_text(scores):
    text = ""
    for score in scores:
        if text == "":
            text = str(score)
        else:
            text = text + ", " + str(score)
    return text


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students):
    name = input("Student name: ")

    student_id = input("Student ID: ")
    if student_id.isdigit() == False:
        print("Student ID must be a number.")
        return
    student_id = int(student_id)

    if find_student(students, student_id) != None:
        print(f"A student with ID {student_id} already exists.")
        return

    how_many = input("How many scores? ")
    if how_many.isdigit() == False:
        print("Please enter a number.")
        return
    how_many = int(how_many)

    if how_many < 1:
        print("A student must have at least one score.")
        return

    scores = []
    for i in range(how_many):
        score = input(f"Enter score {i + 1}: ")
        if score.isdigit() == False:
            print("Scores must be whole numbers. Adding cancelled.")
            return
        scores.append(int(score))

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_students(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average'}")
    print("-" * 50)

    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = scores_as_text(student["scores"])
        avg = average(student["scores"])
        print(f"{name:<15}{student_id:<12}{scores:<15}{avg:.2f}")

    print("-" * 50)


def calculate_average(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return

    student_id = input("Enter student ID: ")
    if student_id.isdigit() == False:
        print("Student ID must be a number.")
        return
    student_id = int(student_id)

    student = find_student(students, student_id)

    if student == None:
        print(f"Error: no student found with ID {student_id}.")
    else:
        avg = average(student["scores"])
        print(f"{student['name']}'s average score: {avg:.2f}")


def main():
    students = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


main()

