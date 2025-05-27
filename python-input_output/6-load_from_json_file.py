#!/usr/bin/python3
"""Importing the JSON module."""
import json


def load_from_json_file(filename):
    """Function that reads data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as a:
        data = json.load(a)
        return data
