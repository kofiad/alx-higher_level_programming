#!/usr/bin/python3
"""A Square class"""


class Square:
    """ Class Square
    Private instance attribute: size
    Instantiation with size
    """
    def __init__(self, size=0, position=0):
        """Constructor method for class
        Initializes "size" and "position" attributes

        Args:
            size (_private int_): _size of the square_
            position (_tuple of 2 positive integers_): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """_Getter method for position attribute_

        Returns:
            _private tuple_: position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position attribute

        Args:
            value (tuple): coordinates of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or
        not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method
        Returns the current squate area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #
        if size is equal to 0, print an empty line
        position should be use by using space
        Do not fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print()
        else:
            print("\n"*self.__position[1], end="")
            for _ in range(self.__size):
                print(" "*self.__position[0] + "#"*self.__size)
