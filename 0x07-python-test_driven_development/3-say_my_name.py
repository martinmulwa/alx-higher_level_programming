#!/usr/bin/python3
""" 3-say_my_name.py """


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name: string representing first name
        last_name: string representing last name

    Returns: None
    """
    # check that first_name and last_name are both strings
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
