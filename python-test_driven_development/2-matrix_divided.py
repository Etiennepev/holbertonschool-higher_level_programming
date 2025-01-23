#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides
all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by `div`.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number to divide each element by.

    Returns:
        list of lists: A new matrix with elements divided by `div`,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
                   or if rows are not of the same size, or if `div` is not
                   an integer or float.
        ZeroDivisionError: If `div` is zero.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix_divided([[1, 2, 3], [4, 5]], 2)
        Traceback (most recent call last):
        ...
        TypeError: Each row of the matrix must have the same size
        >>> matrix_divided(matrix, "School")
        Traceback (most recent call last):
        ...
        TypeError: div must be a number
        >>> matrix_divided(matrix, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
        >>> matrix_divided([[1, 2], ["a", 4]], 2)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats
    """

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        divided_matrix.append(new_row)

    return divided_matrix

# return [[round(x / div, 2) for x in row] for row in matrix]
