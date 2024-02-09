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
        self.__y = y