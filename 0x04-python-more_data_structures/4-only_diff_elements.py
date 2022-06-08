#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Creates a set of all elements present in only one set

    Args:
        set_1: set
        set_2: set

    Return: set
    """
    return (set_1 - set_2) | (set_2 - set_1)
