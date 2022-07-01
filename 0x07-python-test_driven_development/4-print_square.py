#!/usr/bin/python3
""" 4-print_square.py """


def print_square(size):
    """Prints a square with the character #

    Args:
        size: non-negative integer representing size of square

    Returns: None
    """
    # check that size is a non-negative integer
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # just print new line for square of size 0
    if size == 0:
        print("")

    for i in range(size):
        print("#" * size)
