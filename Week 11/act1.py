import unittest

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-7, 2), -14)

if __name__ == '__main__':
    unittest.main()
