#!/usr/bin/python3
"""Defines a class named Square"""


Class Square:
    """
    Class named Square
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """
        This is the constructor method for the class.
        It initializes the 'size' attribute.
        Parameters:
        size (int): The size of the square.
        """
        self.__size = size
