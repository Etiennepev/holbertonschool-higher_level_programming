#!/usr/bin/python3
"""Module: lookup
This module provides a function to retrieve the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
