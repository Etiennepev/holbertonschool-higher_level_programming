#!/usr/bin/python3
"""
Module 4-print_square
Provides a function `print_square` to print square
"""


def print_square(size):
    """
    Prints a square of '#' characters of a given size.

    Args:
        size: The size of the square, must be an integer.

    Returns:
        None

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
