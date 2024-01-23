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
        self.__size = value

    def area(self):
        """Public instance method
        Returns the current squate area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#"*self.__size)
