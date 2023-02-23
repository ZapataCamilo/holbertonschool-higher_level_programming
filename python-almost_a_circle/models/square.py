#!/usr/bin/python3
"""
Name: square
---------------
Class name: Square
---------------
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the class Square by overriding the __str__"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Returns the value of the __width attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value of the __width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    def update(self, *args, **kwargs):
        """Updates the Square class,
        assigning an argument to each attribute.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {"id": self.id,
               "size": self.size,
               "x": self.x,
               "y": self.y
               }
        return dic
