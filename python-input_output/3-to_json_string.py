#!/usr/bin/python3
"""This module contains a function that converts an object to JSON."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string."""
    return json.dumps(my_obj)
