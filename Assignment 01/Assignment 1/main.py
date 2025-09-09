from users import Customer, Admin
from database import db
from tabulate import tabulate 

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (Admin/Customer): ")
    if role not in ["Admin", "Customer"]:
        print("Invalid role!")
        return
    try:
        db.add_user(username, password, role)
        print(f"User {username} registered as {role}.")
    except:
        print("Username already exists.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = db.get_user(username)
    if user and user[2] == password:
        print(f"Login successful. Role: {user[3]}")
        return user
    else:
        print("Invalid credentials.")
        return None

def customer_menu(user):
    customer = Customer(user[1], user[3])
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Available Cars")
        print("2. Book Car")
        print("3. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            customer.view_available_cars()
        elif choice == "2":
            try:
                car_id = int(input("Enter Car ID to book: "))
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                customer.book_car(car_id, start_date, end_date)
            except ValueError:
                print("Invalid input!")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

def admin_menu(user):
    admin = Admin(user[1], user[3])
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Car")
        print("2. Manage Bookings")
        print("3. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            mileage = int(input("Mileage: "))
            min_rent = int(input("Min rent days: "))
            max_rent = int(input("Max rent days: "))
            price = float(input("Price per day: "))
            admin.add_car(make, model, year, mileage, min_rent, max_rent, price)
        elif choice == "2":
            pending = db.get_pending_bookings()
            if not pending:
                print("No pending bookings.")
                continue
            headers = ["Booking ID", "User ID", "Car ID", "Start Date", "End Date", "Total Cost", "Status"]
            print(tabulate(pending, headers=headers, floatfmt=".2f"))
            for b in pending:
                action = input(f"Booking ID {b[0]} - Approve(A) / Reject(R) / Skip(S): ").upper()
                if action == "A":
                    from booking import Booking as B
                    booking = B(*b)
                    booking.approve()
                    print("Booking approved.")
                elif action == "R":
                    from booking import Booking as B
                    booking = B(*b)
                    booking.reject()
                    print("Booking rejected.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

def run():
    while True:
        print("\n=== Welcome to Car Rental System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                if user[3] == "Customer":
                    customer_menu(user)
                else:
                    admin_menu(user)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()
