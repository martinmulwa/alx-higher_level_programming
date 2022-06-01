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
