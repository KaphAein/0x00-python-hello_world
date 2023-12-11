#!/usr/bin/python3
"""Class defining rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""


    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Represents a getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """Represents a setter"""
        self.__width = value
        self.__height = value
        
    def __str__(self):
        """represents infromal print of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                       self.width)

    def update(self, *args, **kwargs):
        """module update square
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Returns a dictionary representation of this class'''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
    
