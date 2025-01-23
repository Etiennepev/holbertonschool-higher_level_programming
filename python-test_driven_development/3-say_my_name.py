#!/usr/bin/python3
"""
Module 3-say_my_name
Provides a function `say_my_name` that prints two names.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>.
    Args:
        first_name (string): first name to print.
        last_name (string): last name to print.
    Raises:
        TypeError: in case of non string type argument.

    Returns:
    None.

    Example :
    >>> say_my_name(John, Wick)
    My name is John Wick

    """
    if not isinstance(first_name, str) or len(first_name) == 0:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
