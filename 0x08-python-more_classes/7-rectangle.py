#!/usr/bin/python3
"""7-rectangle.py"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Creates an instance of Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the value of private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the value of private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Finds the area of the Rectangle

        Returns: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Finds the perimeter of the Rectangle

        Returns: perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of a rectangle """
        if self.width == 0 or self.height == 0:
            return ""

        symbol = str(self.print_symbol)
        result = [symbol * self.width for i in range(self.height)]
        return "\n".join(result)

    def __repr__(self):
        """Internal representation of a rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes an instance of a Rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
