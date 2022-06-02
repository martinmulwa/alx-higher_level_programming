#!/usr/bin/python3

def remove_char_at(str, n):
    """
    Removes a character at a given index in a string

    Args:
        str: string
        n: integer

    Return:
        A copy of the string with the character at index n removed
    """
    return str[:] if n < 0 else str[:n] + str[n + 1:]
