#!/usr/bin/python3
"""Defines a text-writing function"""


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the number of characters written

    Args:
        filename (str, optional): file of interest. Defaults to "".
        text (str, optional): text to be inserted. Defaults to "".

    Returns:
        str: file with updated written text
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)