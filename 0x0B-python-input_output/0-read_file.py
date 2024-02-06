#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str, optional):name of the string. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())