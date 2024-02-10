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