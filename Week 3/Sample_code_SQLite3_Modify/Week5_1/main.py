from database import create_table, create_students_table
from user_manager import (
    add_user, view_users, search_user, delete_user, add_student, view_students
)

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. View Students")
    print("6. Exit")

def main():
    create_table()
    create_students_table()
    students = view_students()
    if len(students) == 0: 
        add_student("Sach", "123 Queen St")
        add_student("Lakshan", "16D Auckland 1061")

    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            print("\n=== Users Table ===")
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("\n=== Students Table ===")
            students = view_students()
            for student in students:
                print(student)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
