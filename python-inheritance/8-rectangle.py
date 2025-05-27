#!/usr/bin/python3
""" BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that derives from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the rectangle's area."""
        return self.__width * self.__height
