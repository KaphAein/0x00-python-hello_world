#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter for attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for attribute position"""
        if (
                not isinstance(value, tuple)
                or not len(value) == 2
                or not all(isinstance(n, int) and n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (value[0], value[1])

    def area(self):
        """Represent area of Square"""
        return self.__size ** 2

    def my_print(self):
        """prints area in #"""
        if not self.__size:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Represents print square"""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print()
        return ""
