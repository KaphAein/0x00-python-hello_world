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

    def update(self, *args, **kwargs)
         '''Updates the arguments in the class'''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''Returns a dictionary representation of this class'''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
    
