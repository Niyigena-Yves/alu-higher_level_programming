#!/usr/bin/python3
"""This module defines the BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that extends BaseGeometry."""
    def __init__(self, width, height):
        """Initialize the rectangle using width and height."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Provide a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
