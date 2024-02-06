#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of the student class

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of a Student instance

        Returns:
            dictionary: representation of a Student instance
        """
        if (isinstance(attrs, list) and
                all(isinstance(element, str) for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json (dictionary): values to replace attributes with
        """
        for key, value in json.items():
                setattr(key, value)
