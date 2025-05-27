#!/usr/bin/python3
"""
Module 2-is_same_class
Defines a function.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is an instance of a_class, else False.
    """
    return type(obj) is a_class
