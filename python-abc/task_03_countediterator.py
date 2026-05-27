#!/usr/bin/python3
"""This module defines a CountedIterator class."""


class CountedIterator:
    """Custom iterator that counts iterated items."""

    def __init__(self, iterable):
        """Initialises the iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Return next item and increment counter."""
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Return number of iterated items."""
        return self.counter
