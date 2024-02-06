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
        
    def to_json(self):
        """retrieves dictionary representation of a Student instance

        Returns:
            dictionary: representation of a Student instance
        """
        return self.__dict__