#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """appends a string to the end of a text file and returns the number of characters added

    Args:
        filename (str, optional): text file of interest. Defaults to "".
        text (str, optional): text to be appended. Defaults to "".

    Returns:
        str: file with appended text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)