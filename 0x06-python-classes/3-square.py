#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """Defines attribute size of a Square"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

        def area(self):
            """Represent area of Square"""
            return (self.__size * self.__size)
