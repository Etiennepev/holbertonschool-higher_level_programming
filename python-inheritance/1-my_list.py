#!/usr/bin/python3
"""
Module: my_list
This module defines a custom list class that inherits from the built-in list.
"""


class MyList(list):
    """
    A subclass of list that adds a method to print a
    sorted version of itself.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
