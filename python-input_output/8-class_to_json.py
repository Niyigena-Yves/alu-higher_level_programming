#!/usr/bin/python3
"""
This module contains a function to return the dictionary description for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
