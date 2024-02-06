#!/usr/bin/python3
"""Defines a load_from_json_file function"""
import json


def load_from_json_file(filename):
    """ creates an object from a JSON file in Python

    Args:
        filename (str): text file

    Returns:
        str: object from json file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)