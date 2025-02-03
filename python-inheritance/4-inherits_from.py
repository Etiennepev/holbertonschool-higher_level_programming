#!/usr/bin/python3
"""
Module: inherits from
This module inherits
"""


def inherits_from(obj, a_class):
    """
    Prints the list in ascending order.

    This method sorts the list and prints the sorted version, leaving the
    original list unchanged.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
