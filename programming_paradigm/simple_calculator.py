class SimpleCalculator:
    """A simple calculator class for basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Return the division of two numbers.
        
        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
