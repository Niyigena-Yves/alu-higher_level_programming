#!/usr/bin/python3
"""Defines the inherited list class MyList."""


class MyList(list):
    """This sorts the list class."""

    def print_sorted(self):
        """This prints the list in ascending order."""
        print(sorted(self))
