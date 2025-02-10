#!/usr/bin/python3
"""
Module: read file
Provides 'Read file'
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.
    """
    with open(filename, "r", encoding="utf-8") as f:
            print(f.read(), end="")
