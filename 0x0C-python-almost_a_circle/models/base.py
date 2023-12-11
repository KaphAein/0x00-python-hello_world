#!/usr/bin/python3
"""Class defining base"""
import json
import csv


class Base:
    """Represents a base"""

    __nb_objects = 0

    def __init__(self, id=None)
        """Initialize a new base"""
        if id:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

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

    def bigger_or_equal(rect_1, rect_2):
        """represents inequality"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """represents a square"""
        return cls(size, size)

    def __str__(self):
        """represents infromal print of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        ret = []
        for i in range(self.__height):
            for j in range(self.__width):
                ret.append(str(self.print_symbol))
            if not i == self.height - 1:
                ret.append("\n")
        return "".join(ret)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes class and sends a message afterwards"""
        print("Bye rectangle...")
        type(self).__nb_objects -= 1
