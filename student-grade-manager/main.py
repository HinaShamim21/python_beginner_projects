students={}

def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print(f"Student ID {student_id} already exists.")
        return
    name = input("Enter student name: ")
    students[student_id] = {"name": name, "grades": []}
    print(f"Student added successfully: {student_id}")

def add_grade():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    grade = float(input("Enter grade: "))
    students[student_id]["grades"].append(grade)
    print(f"Grade added successfully for student ID {students[student_id]['name']}.")


def view_student():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    student = students[student_id]
    print(f"Student ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Grades: {student['grades']}")

def calculate_average():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    grades = students[student_id]["grades"]
    if not grades:
        print(f"No grades available for student ID {student_id}.")
        return
    average = sum(grades) / len(grades)
    print(f"Average grade for student ID {student_id}: {average:.2f}")

def find_highest_lowest():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    grades = students[student_id]["grades"]
    if not grades:
        print(f"No grades available for student ID {student_id}.")
        return
    highest = max(grades)
    lowest = min(grades)
    print(f"Highest grade for student ID {student_id}: {highest}")
    print(f"Lowest grade for student ID {student_id}: {lowest}")


def view_all_students():
    if not students:
        print("No students available.")
        return
    for student_id, student in students.items():
        print(f"Student ID: {student_id}, Name: {student['name']}, Grades: {student['grades']}")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student")
        print("4. Calculate Average Grade")
        print("5. Find Highest and Lowest Grade")
        print("6. View All Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_grade()
        elif choice == '3':
            view_student()
        elif choice == '4':
            calculate_average()
        elif choice == '5':
            find_highest_lowest()
        elif choice == '6':
            view_all_students()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()