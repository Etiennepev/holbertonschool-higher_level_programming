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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def area(self):
        	return self.__size**2
