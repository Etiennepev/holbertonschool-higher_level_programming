#!/usr/bin/python3
"""
Module containing the definition of the Square class.

This module provides a placeholder for a Square class that can be expanded
to represent a square and its related properties or behaviors.
"""


class Square:
    """
    Representation of a square.
    """
    def __init__(self, size=0):
        """
        Initializes a square with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        return self.__size**2
