#!/usr/bin/python3
"""Defines a lookup class"""

def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
        obj : object

    Returns:
        list : object
    """
    return dir(obj)