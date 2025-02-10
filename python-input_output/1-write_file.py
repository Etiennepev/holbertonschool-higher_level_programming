#!/usr/bin/python3
"""
Module: write file
Provides 'write file'
"""


def write_file(filename="", text=""):
    """
    Write in a text file (UTF-8) and prints its content to stdout.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
