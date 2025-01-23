#!/usr/bin/python3
"""
Module 2-matrix_divided
Provides a function `matrix_divided` to divide a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a perfect matrix.
    Args:
        matrix (list): list of integer or float to divide.
        div (float or int): number to divide with.
    Raises:
        TypeError: in case of non int or non float type argument.
        TypeError: if each row of the matrix ain't the same size.
        TypeError: if div isn't a number.
        ZeroDivisionError: if div is zero.

    Returns:
    list of lists: return a new matrix rounded to 2 decimal places.

    Example :
    >>> matrix_divided((example_list([1, 2, 3], [1, 2, 3]), 1))
    [1, 2, 3], [1, 2, 3]

    """

    error_txt = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_txt)
    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(error_txt)
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)
    return new_matrix
