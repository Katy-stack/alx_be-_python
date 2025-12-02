# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division, handling ZeroDivisionError and ValueError.
    """
    try:
        # 1. Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # 2. Attempt to perform the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Catches division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Catches non-numeric input
        return "Error: Please enter numeric values only."