#!/usr/bin/python3
"""
Module: append file
Provides 'append file'
"""


def append_write(filename="", text=""):
    """
    Append in a text file (UTF-8) and prints its content to stdout.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
