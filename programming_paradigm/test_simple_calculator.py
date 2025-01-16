import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(-2, 3), -5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_edge_cases(self):
        """Test edge cases for all methods."""
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)  # Large numbers
        self.assertEqual(self.calc.subtract(1e-10, 1e-10), 0)  # Small numbers
        self.assertEqual(self.calc.multiply(1e10, 1e-10), 1)  # Small x Large
        self.assertEqual(self.calc.divide(1e10, 1e10), 1)  # Large numbers


if __name__ == "__main__":
    unittest.main()
