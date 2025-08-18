from database import create_tables
from manager import (
    add_student, view_students, delete_student,
    add_course, view_courses
)

def menu():
    print("\n==== YB College Database ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Exit")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            name = input("Enter student name: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            gender = input("Enter gender: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            add_student(name, dob, gender, email, phone)

        elif choice == '2':
            print("\n=== Students ===")
            for s in view_students():
                print(s)

        elif choice == '3':
            sid = int(input("Enter StudentID to delete: "))
            delete_student(sid)

        elif choice == '4':
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            semester = input("Enter semester: ")
            add_course(name, credit, semester)

        elif choice == '5':
            print("\n=== Courses ===")
            for c in view_courses():
                print(c)

        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
