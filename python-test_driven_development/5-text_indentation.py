#!/usr/bin/python3
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
            # Skip any spaces immediately following these characters
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
        i += 1
