#!/usr/bin/python3
"""This module creates the Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """
    A class named Rectangle
    Attributes:
             attr1(id): id of object
             attr2(width): rectangle width
             attr3(height): rectangle height
             attr4(x): number of spaces before rectangle
             attr5(y): number of newlines before rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
