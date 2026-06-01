#!/usr/bin/python3
"""This module contains a function that writes text to a file."""


def write_file(filename="", text=""):
    """Write a string to UTF-8 text file and return characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
