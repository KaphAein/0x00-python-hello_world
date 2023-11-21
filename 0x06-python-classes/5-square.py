#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """Defines attribute size of a Square"""
        self.__size = size

    @property
    def size(self):
        """getter for attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for attribute size"""
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """Represent area of Square"""
        return self.__size ** 2

    def my_print(self):
        """prints area in #"""
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
