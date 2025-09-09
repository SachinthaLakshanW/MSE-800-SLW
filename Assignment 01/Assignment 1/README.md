Car Rental System
Overview

The Car Rental System is a command-line application developed in Python. It provides functionality for customers to register, log in, view available cars, and make bookings. Administrators can add cars and manage bookings, including approval and rejection.

The system is implemented using Object-Oriented Programming (OOP) principles, SQLite for persistent data storage, and standard design patterns to ensure modularity and maintainability.

Installation and Setup
Requirements:
Python 3.10 or higher
SQLite (included with Python)

Steps:
Clone or download the project folder.
Navigate to the project directory.

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
Windows (PowerShell): venv\Scripts\Activate.ps1
macOS/Linux: source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the application:
python main.py

Project Structure

Assignment-1/
main.py (Entry point, system menus)
users.py (User, Customer, Admin classes)
car.py (Car class)
booking.py (Booking class)
database.py (Database operations)
requirements.txt (Dependencies)
README.txt (Documentation)

User Documentation
Customer Functions:
Register a new account
Log in to the system
View available cars
Book a car with rental duration
Log out

Administrator Functions:
Log in as Admin
Add cars to the system
View and manage bookings (approve or reject)
Log out
Error Handling
Invalid login credentials are rejected with an error message.
If no cars exist in the system, the user is informed.
If no pending bookings exist, the administrator is informed.
Invalid menu options are handled with prompts to retry.

License
This project is released under the MIT License.
It may be used, modified, and distributed with proper attribution.

Known Issues
The system is CLI-based; no graphical interface is available.
Administrators can register themselves rather than being pre-assigned.
No payment gateway integration; booking is limited to system confirmation.

Credits

Developer: Weerakkody Gamage Sachintha Lakshan Weerakkody
Programme: Master of Software Engineering
Course: MSE800 – Professional Software Engineering
Institution: Yoobee College of Creative Innovation
Date: 2025/09/14