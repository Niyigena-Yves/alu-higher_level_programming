#!/usr/bin/python3
"""this module defines a square class"""


class Square:
    """defines a square with validation for size"""

    def __init__(self, size=0):
        """initializes the size of the square"""
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
