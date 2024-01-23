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
            size (_private int_): _size of the square_
        """
        self.__size = size

    def area(self):
        """Public instance method
        Returns the current squate area
        """
        return self.__size ** 2

    @property
    def size(self):
        """_Getter method for size attribute_

        Returns:
            _private int_: _size of square_
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute

        Args:
            value (int): _descript_

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
