import sqlite3
import threading
import time

start_time = time.time()

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._connection = None
        return cls._instance

    def get_connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect('app.db', check_same_thread=False)
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None

conn = DatabaseConnection().get_connection()
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER, product TEXT)")
cur.execute("INSERT OR IGNORE INTO users VALUES (1, 'Alice')")
cur.execute("INSERT OR IGNORE INTO orders VALUES (1, 1, 'Laptop')")
cur.execute("INSERT OR IGNORE INTO orders VALUES (2, 1, 'Mouse')")
conn.commit()

class UserService:
    def get_user(self, user_id):
        conn = DatabaseConnection().get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cur.fetchone()

class OrderService:
    def get_orders(self, user_id):
        conn = DatabaseConnection().get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        return cur.fetchall()

user_service = UserService()
order_service = OrderService()

print("User:", user_service.get_user(1))
print("Orders:", order_service.get_orders(1))

end_time = time.time()
print(f"Execution time: {end_time - start_time:.6f} seconds")