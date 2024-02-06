#!/usr/bin/python3
import json
"""Defines a string-to-JSON function"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string) in Python

    Args:
        my_obj (string): object string

    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
