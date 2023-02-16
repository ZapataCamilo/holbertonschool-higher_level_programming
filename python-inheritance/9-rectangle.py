#!/usr/bin/python3
"""
Write a class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

class Rectangle(BaseGeometry):
    """
      class Rectangle that inherits from
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        try:
            super().bg.area()
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
