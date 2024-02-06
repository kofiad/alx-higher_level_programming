#!/usr/bin/python3
"""Defines a JSON-to-string function"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string in Python

    Args:
        my_str (string): object

    Returns:
         Python data structure: converted JSON string to a Python data structure
    """
    return json.loads(my_str)