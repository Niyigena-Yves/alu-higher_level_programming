#!/usr/bin/python3
"""Importing the JSON module."""
import json


def from_json_string(my_str):
    """Converts a JSON string back into a Python object."""
    return json.loads(my_str)
