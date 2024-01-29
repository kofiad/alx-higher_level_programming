#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a square
    """
    def __init__(self, width=0, height=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self.__width = width
        self.__height =height

    @property
    def width(self):
        """to retrieve width of rectangle

        Returns:
            int: width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve height of rectangle

        Returns:
            int: height of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value