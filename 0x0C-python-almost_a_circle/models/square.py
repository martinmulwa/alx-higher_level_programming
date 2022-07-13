#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class the inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square object"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the attributes of the Square object"""
        attrs = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        attrs = ["id", "size", "x", "y"]
        return {s: getattr(self, s) for s in attrs}
