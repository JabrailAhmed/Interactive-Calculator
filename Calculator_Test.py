import unittest


from Calculator import add, subtract, multiply, divide


class TestInteractiveCalculator(unittest.TestCase):

    def test_addition(self):
        """Test that the addition function correctly sums two numbers."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertAlmostEqual(add(5.5, 2.3), 7.8)

    def test_subtraction(self):
        """Test that the subtraction function correctly deducts two numbers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(5, 10), -5)

    def test_multiplication(self):
        """Test that multiplication returns the correct product."""
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(5, 0), 0)

    def test_division(self):
        """Test standard division operations."""
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-12, 3), -4)

    def test_divide_by_zero(self):
        """Test that dividing by zero handles gracefully or raises an appropriate error."""
        # If your code raises a ZeroDivisionError, use this:
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

        # NOTE: If your calculator code handles zero division by returning a string
        # (like "Error: Cannot divide by zero"), uncomment the line below instead:
        # self.assertEqual(divide(10, 0), "Error: Cannot divide by zero")


if __name__ == '__main__':
    unittest.main()
