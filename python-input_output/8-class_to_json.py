#!/usr/bin/python3
"""This module contains a function that returns a dictionary description."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
