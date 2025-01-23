#!/usr/bin/python3
"""
Module 5-text_indentation
Provides a function `text_indentation` to indentate text.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="")
            print("\n")
            print("")
            i += 1
        else:
            print(text[i], end="")
        i += 1
