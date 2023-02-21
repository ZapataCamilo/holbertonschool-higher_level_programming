#!/usr/bin/python3
from models.base import Base
"""
Name: rectangle
---------------
Class name: Rectangle
---------------
"""


class Rectangle(Base):
    """
    this class give us a id, width and height
    for the object
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Here we ask if there are id, width and height
        if not put of id one with the private class attribute __nb_objects
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def public_set(self):
        return (self.__width, self.__height, self.__x, self.__y)

    @public_set.setter
    def public_set(self):
        return (self.width, self.height, self.x, self.y)
