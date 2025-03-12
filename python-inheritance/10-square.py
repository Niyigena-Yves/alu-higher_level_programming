#!/usr/bin/python3
"""This module defines the BaseGeometry class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that extends Rectangle."""
    def __init__(self, size):
        """Initialize the square using its size."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
