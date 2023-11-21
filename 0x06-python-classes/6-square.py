#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Defines attribute size of a Square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter for attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for attribute position"""
        if isinstance(value, tuple) and len(value) == 2 and value[0] >= 0 and value[1] >= 0:
            self.__position = (value[0], value[1])
        elif not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            pass

    def area(self):
        """Represent area of Square"""
        return self.__size ** 2

    def my_print(self):
        """prints area in #"""
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0])
                for j in range(self.__size):
                    print("#", end="")
                print()
