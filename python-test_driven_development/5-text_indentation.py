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

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    
    # Printing the formatted result without leading or trailing spaces on each line
    lines = result.split('\n')
    formatted_lines = [line.strip() for line in lines]
    formatted_text = '\n'.join(formatted_lines)
    print(formatted_text)
