#!/usr/bin/python3
"""Module for the Rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """constructor function"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle's width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle's height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
