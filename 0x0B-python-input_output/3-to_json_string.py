#!/usr/bin/python3
"""Defines a JSON representation function"""

import json
def to_json_string(my_obj):
    """returns the JSON representation of an object (string) in Python

    Args:
        my_obj (string): object string

    Returns:
        string: JSON representation
    """
    return json.dumps(my_obj)