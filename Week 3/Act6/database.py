import sqlite3

def create_connection():
    conn = sqlite3.connect("college.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            DOB TEXT,
            Gender TEXT,
            Email TEXT UNIQUE,
            Phone TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturers (
            LecturerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Department TEXT,
            Email TEXT UNIQUE,
            Phone TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Credit INTEGER,
            Semester TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Classes (
            ClassID INTEGER PRIMARY KEY AUTOINCREMENT,
            CourseID INTEGER,
            LecturerID INTEGER,
            Schedule TEXT,
            Room TEXT,
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
            FOREIGN KEY (LecturerID) REFERENCES Lecturers(LecturerID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teaches (
            LecturerID INTEGER,
            ClassID INTEGER,
            PRIMARY KEY (LecturerID, ClassID),
            FOREIGN KEY (LecturerID) REFERENCES Lecturers(LecturerID),
            FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attend (
            StudentID INTEGER,
            ClassID INTEGER,
            PRIMARY KEY (StudentID, ClassID),
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
            FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
        )
    ''')

    conn.commit()
    conn.close()
