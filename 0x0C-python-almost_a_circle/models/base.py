#!/usr/bin/python3
""" Base """


class Base:
    """Base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
