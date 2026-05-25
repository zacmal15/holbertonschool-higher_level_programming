#!/usr/bin/python3
"""This module defines a function thay checks object type."""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of a_class."""
    return type(obj) is a_class
