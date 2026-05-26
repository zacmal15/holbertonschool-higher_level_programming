#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """This class inherits from list and prints a sorted list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
