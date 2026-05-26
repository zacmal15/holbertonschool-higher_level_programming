#!/bin/usr/python3
"""This module defines a function that checks inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherited class."""
    return isinstance(obj, a_class)
