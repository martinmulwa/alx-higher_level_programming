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

    for i in range(n):
        c = ord(str[i]) - 32 if islower(str[i]) else ord(str[i])

        if i < n - 1:
            print("{:c}".format(c), end="")
        else:
            print("{:c}".format(c))
