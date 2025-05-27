#!/usr/bin/python3
"""Script that adds command-line arguments to
a Python list and saves them to a file."""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

try:
    # Load existing data from the file
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    json_list = []

# Append only the arguments, excluding the script name
for arg in argv[1:]:
    json_list.append(arg)

# Save the updated list to the file
save_to_json_file(json_list, filename)
