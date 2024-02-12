#!/usr/bin/python3
"""Defines a base class"""
import json


class Base:
    """Base class initialization
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list):  is a list of dictionaries

        Returns:
            JSON string : representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (string): a string representing a list of dictionaries

        Returns:
            list: JSON string representation
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)