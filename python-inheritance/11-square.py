#!/usr/bin/python3
"""
Module: Square
This module initialize a Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initialize a Square instance.

    Args:
        size (int): The size of the Square. Default is 0.
    """
    def __init__(self, size):
        super().integer_validator(size, size)
        self.__size = size

    def area(self):
        return self.__size**2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
