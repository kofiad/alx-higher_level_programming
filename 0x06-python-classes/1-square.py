#!/usr/bin/python3
"""A Square class"""


class Square:
    """ Class Square
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """Constructor method for class
        Initializes "size" attribute

        Args:
            size (_private_): _size of the square_
        """
        self.__size = size
