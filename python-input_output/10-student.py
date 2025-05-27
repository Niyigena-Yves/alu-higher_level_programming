#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """Representation of a Student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the student's attributes as a dictionary."""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
