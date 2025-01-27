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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        for i in range(self.__size):
            if self.__size > 0:
                print("#" * self.__size)
            else:
                print()
