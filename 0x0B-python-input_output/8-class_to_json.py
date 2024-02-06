#!/usr/bin/python3
"""Defines a class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure for
    JSON serialization of an object

    Args:
        obj :  an instance of a class

    Returns:
        dictionary description of obj
    """
    return obj.__dict__