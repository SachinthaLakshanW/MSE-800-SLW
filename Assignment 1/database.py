import sqlite3

class Database:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name="car_rental.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Users table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
        """)
        # Cars table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT,
            model TEXT,
            year INTEGER,
            mileage INTEGER,
            available INTEGER,
            min_rent_days INTEGER,
            max_rent_days INTEGER,
            price_per_day REAL
        )
        """)
        # Bookings table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            car_id INTEGER,
            start_date TEXT,
            end_date TEXT,
            total_cost REAL,
            status TEXT DEFAULT 'Pending'
        )
        """)
        self.conn.commit()

    # --- User Methods ---
    def add_user(self, username, password, role):
        self.cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                            (username, password, role))
        self.conn.commit()

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return self.cursor.fetchone()

    # --- Car Methods ---
    def add_car(self, make, model, year, mileage, available, min_rent_days, max_rent_days, price_per_day):
        self.cursor.execute("""
            INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, price_per_day)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (make, model, year, mileage, available, min_rent_days, max_rent_days, price_per_day))
        self.conn.commit()

    def get_all_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        return self.cursor.fetchall()

    def get_available_cars(self):
        self.cursor.execute("SELECT * FROM cars WHERE available=1")
        return self.cursor.fetchall()

    def update_car_availability(self, car_id, available):
        self.cursor.execute("UPDATE cars SET available=? WHERE id=?", (available, car_id))
        self.conn.commit()

    # --- Booking Methods ---
    def add_booking(self, user_id, car_id, start_date, end_date, total_cost):
        self.cursor.execute("""
            INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost)
            VALUES (?, ?, ?, ?, ?)""",
            (user_id, car_id, start_date, end_date, total_cost))
        self.conn.commit()

    def get_pending_bookings(self):
        self.cursor.execute("SELECT * FROM bookings WHERE status='Pending'")
        return self.cursor.fetchall()

    def update_booking_status(self, booking_id, status):
        self.cursor.execute("UPDATE bookings SET status=? WHERE id=?", (status, booking_id))
        self.conn.commit()

# Singleton instance
db = Database()
