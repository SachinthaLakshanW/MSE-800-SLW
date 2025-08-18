from database import create_connection
import sqlite3

# ==== STUDENTS ====
def add_student(name, dob, gender, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (Name, DOB, Gender, Email, Phone) VALUES (?, ?, ?, ?, ?)",
                   (name, dob, gender, email, phone))
    conn.commit()
    conn.close()
    print("Student added successfully.")

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")

# ==== COURSES ====
def add_course(name, credit, semester):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Courses (Name, Credit, Semester) VALUES (?, ?, ?)",
                   (name, credit, semester))
    conn.commit()
    conn.close()
    print("Course added successfully.")

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Courses")
    rows = cursor.fetchall()
    conn.close()
    return rows
