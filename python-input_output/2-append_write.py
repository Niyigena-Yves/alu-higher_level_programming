#!/usr/bin/python3
"""Create a function that adds a string to the end of a file
and returns the count of characters appended."""


def append_write(filename="", text=""):
    """Function that appends content to a file."""
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
