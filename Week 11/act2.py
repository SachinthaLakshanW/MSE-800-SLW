import sqlite3, unittest

class ExpenseTracker:
    def __init__(self, db="expenses.db"):
        self.conn = sqlite3.connect(db)
        self.conn.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, description TEXT, amount REAL)")
        self.conn.commit()

    def add_expense(self, desc, amount):
        self.conn.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (desc, amount))
        self.conn.commit()

    def total_expense(self):
        cur = self.conn.cursor()
        cur.execute("SELECT SUM(amount) FROM expenses")
        result = cur.fetchone()[0]
        return result or 0

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.t = ExpenseTracker(":memory:")

    def test_add_and_total(self):
        self.t.add_expense("Lunch", 10)
        self.t.add_expense("Bus", 5)
        self.assertEqual(self.t.total_expense(), 15)

    def test_empty(self):
        self.assertEqual(self.t.total_expense(), 0)

if __name__ == "__main__":
    unittest.main()
