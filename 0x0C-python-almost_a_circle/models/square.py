#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle

    Args:
        Rectangle : parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        note = "[Square] ({}) {}/{} - {}"
        return note.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter

        Returns:
            int : size of square
        """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__
