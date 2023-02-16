#!/usr/bin/python3
"""
Write a class BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
      class Square that inherits from Rectangle
    """

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self) -> str:
        return f"[Square] {self.__size}/{self.__size}"
