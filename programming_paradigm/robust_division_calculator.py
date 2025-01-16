# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers with error handling.

    Args:
        numerator (str): The numerator, provided as a string.
        denominator (str): The denominator, provided as a string.

    Returns:
        str: Result of division or an appropriate error message.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
