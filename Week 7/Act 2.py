import sqlite3
import time

start_time = time.time()

conn = sqlite3.connect("app.db")
cur = conn.cursor()

def new_func(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER, product TEXT)")
    cur.execute("INSERT OR IGNORE INTO users VALUES (1, 'Alice')")
    cur.execute("INSERT OR IGNORE INTO orders VALUES (1, 1, 'Laptop')")
    cur.execute("INSERT OR IGNORE INTO orders VALUES (2, 1, 'Mouse')")

new_func(cur)
conn.commit()
conn.close()

class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cur.fetchone()
        conn.close()
        return user

class OrderService:
    def get_orders(self, user_id):
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = cur.fetchall()
        conn.close()
        return orders

user_service = UserService()
order_service = OrderService()

print("User:", user_service.get_user(1))
print("Orders:", order_service.get_orders(1))

end_time = time.time()
print(f"Execution time: {end_time - start_time:.6f} seconds")