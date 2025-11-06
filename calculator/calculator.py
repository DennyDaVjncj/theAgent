"""Basic calculator functions."""

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def sub(a: float, b: float) -> float:
    """Return the difference a - b."""
    return a - b


def mul(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def div(a: float, b: float) -> float:
    """Return the quotient a / b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
