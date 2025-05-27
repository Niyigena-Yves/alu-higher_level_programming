#!/usr/bin/python3
"""Importing necessary modules."""
import json


def save_to_json_file(my_obj, filename):
    """Function that saves an object to a JSON file."""
    with open(filename, "w", encoding="utf-8") as a:
        json.dump(my_obj, a)
