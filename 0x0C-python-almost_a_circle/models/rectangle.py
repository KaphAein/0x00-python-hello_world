#!/usr/bin/python3
"""Class defining rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Represents a getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Represents a setter"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Represents a getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Represents a setter"""
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """represents area of rectangle"""
        return self.__y * self.__width


    def display(self):
        '''Prints to stdout the representation of the rectangle'''
        rect = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")
        
    def __str__(self):
        """represents infromal print of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''Updates the arguments in the class'''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''Returns a dictionary representation of this class'''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
