#!/usr/bin/python3
"""this module defins a square class"""


class Square:
    """defines a squar with position atrebute"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the siez and position of the squar"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size with validashun"""
        if type(value) is not int:
            raise TypeError("size must be an intiger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position with validashun"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive intigers")
        self.__position = value

    def area(self):
        """returns the area of the squar"""
        return self.__size ** 2

    def my_print(self):
        """prints the squar using the # charactar with position"""
        if self.__size == 0:
            print()
            return
        print("" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
