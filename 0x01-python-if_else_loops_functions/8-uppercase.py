#!/usr/bin/python3

def islower(c):
    """
    Checks if a given character is in lowercase
    Arguments:
        c: character
    Return:
        True if c is lowercase. False otherwise
    """
    return ord('a') <= ord(c) <= ord('z')


def uppercase(str):
    """
    Prints a string in uppercase followed by a new line
    Arguments:
        str: string
    Return:
        None
    """
    n = len(str)

    for c in str:
        value = ord(c) - 32 if islower(c) else ord(c)
        print("{:c}".format(value), end="")

    print()
