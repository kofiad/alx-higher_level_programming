#!/usr/bin/python3
import json
"""Defines a save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using a JSON representation in Python

    Args:
        my_obj (str): object
        filename (str): text file

    Returns:
        json representation
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
