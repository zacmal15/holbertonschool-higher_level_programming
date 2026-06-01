#!/usr/bin/python3
"""This module contains a function that saves an object to a JSON file."""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
