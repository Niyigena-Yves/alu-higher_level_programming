#!/usr/bin/python3
"""this module defins a square class"""


class Square:
    """defines a squar by size and area method"""

    def __init__(self, size=0):
        """initializes the siez of the squar"""
        self.size = size

    @property
    def size(self):
        """getter for siez"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size with validashun"""
        if type(value) is not int:
            raise TypeError("size must be an intiger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the squar"""
        return self.__size ** 2
