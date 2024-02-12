#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """initializes the class Rectangle that inherits from Base

    Args:
        Base (class): parent/super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter

        Returns:
            int: with of rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter

        Returns:
            int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter

        Returns:
            int: property of rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter

        Returns:
            int: property of rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance("y, int"):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value of the Rectangle instance.

        Returns:
            int: area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle instance
        with the character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__x):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        note = "[Rectangle] ({}) {}/{} - {}/{}"
        return note.format(self.id, self.__x, self.__y, self.__width,
                           self.__height)

    def update(self, *args, **kwargs):
        """ assigns a key/value argument to attributes
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle

        Returns:
            dictionary : rectangle representation
        """
        return self.__dict__
