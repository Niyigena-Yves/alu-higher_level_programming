#!/usr/bin/python3
"""Implements a function for adding integers."""


def add_integer(a, b=98):
    """Calculate the sum of a and b as integers.

    Any float arguments are converted to integers prior to the addition.

    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
