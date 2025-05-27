#!/usr/bin/python3
"""a function that writes string"""


def write_file(filename="", text=""):
    """ writing function"""
    with open(filename, "w", encoding="utf-8") as me:
        num = me.write(text)
        return num
