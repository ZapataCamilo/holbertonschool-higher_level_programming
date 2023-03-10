#!/usr/bin/python3
"""
Name: rectangle
---------------
Class name: Rectangle
---------------
"""

from models.base import Base


class Rectangle(Base):
    """
    this class give us a id, width and height
    for the object
    width: An integer representing the width of the rectangle.
    height: An integer representing the height of the rectangle.
    x: An integer representing the x coordinate of the rectangle.
    Default is 0.
    y: An integer representing the y coordinate of the rectangle.
    Default is 0.
    id: An integer representing the unique identifier of the rectangle.
    Default is None.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Here we ask if there are id, width and height
        if not put of id one with the private class attribute __nb_objects
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the value of the __width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the __width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Returns the value of the __width attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the __width attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Returns the value of the __width attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of the __width attribute"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Returns the value of the __width attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of the __width attribute"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.width

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print('')
        for y in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self) -> str:
        """ the class Rectangle by overriding the __str__"""
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '\
            f'{self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Updates the Rectangle class,
        assigning an argument to each attribute."""
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.width = args[1]
            if len(args) == 3:
                self.height = args[2]
            if len(args) == 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation
        of a Rectangle"""
        dic = {"id": self.id,
               "width": self.__width,
               "height": self.__height,
               "x": self.x,
               "y": self.y
               }
        return dic
