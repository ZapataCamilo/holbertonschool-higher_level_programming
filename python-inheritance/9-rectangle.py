#!/usr/bin/python3
"""
Write a class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
      class Rectangle that inherits from
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self) -> str:
        return f"[Rectangle] {self.__width}/{self.__height}"
