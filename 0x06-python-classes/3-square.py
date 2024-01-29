#!/usr/bin/python3
"""A Square class"""


class Square:
    """ Class Square
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size=0):
        """Constructor method for class
        Initializes "size" attribute

        Args:
            size (_private_): _size of the square_
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method
        Returns the current squate area
        """
        return self.__size ** 2
