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
        """Getter for the width attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
