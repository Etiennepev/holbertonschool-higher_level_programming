#!/usr/bin/python3
"""
Module: base geometry
This module is an empty class
"""


class BaseGeometry:
    """
    Empty class
    """
    def area(self):
        """
        Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
