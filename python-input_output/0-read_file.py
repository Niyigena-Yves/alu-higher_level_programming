#!/usr/bin/python3
"""function that reads files"""


def read_file(filename=""):
    """reading file """
    with open(filename, encoding="utf-8") as a:
        print("{}".format(a.read()), end="")
