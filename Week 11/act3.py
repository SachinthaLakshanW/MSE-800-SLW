class ExpenseTracker:
    """
    >>> t = ExpenseTracker()
    >>> t.add_expense("Lunch", 10)
    >>> t.add_expense("Bus", 5)
    >>> t.total_expense()
    15
    >>> ExpenseTracker().total_expense()
    0
    """
    def __init__(self):
        self.expenses = []

    def add_expense(self, desc, amount):
        self.expenses.append((desc, amount))

    def total_expense(self):
        return sum(amount for _, amount in self.expenses)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
