import unittest

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, desc, amount):
        self.expenses.append((desc, amount))

    def total_expense(self):
        return sum(amount for desc, amount in self.expenses)

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.t = ExpenseTracker()

    def test_add_and_total(self):
        self.t.add_expense("Lunch", 10)
        self.t.add_expense("Bus", 5)
        self.assertEqual(self.t.total_expense(), 15)

    def test_empty(self):
        self.assertEqual(self.t.total_expense(), 0)

if __name__ == "__main__":
    unittest.main()
