#!/usr/bin/python3
"""10-student Module
"""


def is_valid_str_list(lst):
    """Checks if the given list is a list of strings

    Args:
        lst: list

    Returns: True if all the elements in the list are strings. Otherwise False
    """
    return type(lst) == list and all([type(s) == str for s in lst])


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises the first_name, last_name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if not is_valid_str_list(attrs):
            return vars(self)

        return {key: value for key, value in vars(self).items()
                if key in attrs}
