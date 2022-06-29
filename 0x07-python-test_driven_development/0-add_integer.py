#!/usr/bin/python3
"""0-add_integer.py"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: 1st integer
        b: 2nd integer

    Returns: Sum of a and b
    """
    # check that a and b are either integer or float
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # try to convert to integers
    try:
        a = int(a)
    except Exception:
        raise ValueError("cannot convert a to an integer")

    try:
        b = int(b)
    except Exception:
        raise ValueError("cannot convert b to an integer")

    return a + b
