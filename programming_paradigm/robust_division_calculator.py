def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.
    
    Converts inputs to float and handles:
    - Non-numeric input (ValueError)
    - Division by zero (ZeroDivisionError)
    
    Returns formatted result or error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
