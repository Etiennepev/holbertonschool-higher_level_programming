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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): A tuple of two positive integers defining
                              the position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is negative or if the elements of position are not positive integers.
        """
        self.size = size
        self.position = position
        
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
                print("")
        for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

