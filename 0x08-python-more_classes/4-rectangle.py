#!/usr/bin/python3
"""Class defining rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Represents a getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Represents a setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Represents a getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Represents a setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """represents area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """represents perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """represents infromal print of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        ret = []
        for i in range(self.__height):
            for j in range(self.__width):
                ret.append("#")
            if not i == self.height - 1:
                ret.append("\n")
        return "".join(ret)

    def __repr__(self):
        """return a string representation of the rectangle"""
        ret = "Rectangle({}, {})".format(self.__width, self.__height)
