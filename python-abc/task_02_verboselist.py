#!/usr/bin/python3
"""This module defines a VerboseList class."""


class VerboseList(list):
    """Custom list class with notifications."""

    def append(self, item):
        """Add item to list ad print notification."""
        super().append(item)
        print("Added {} to the list.".format(item))
        
    def extend(self, items):
        """Extend list and print notification."""
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        """Remove item from list and print notification."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list and print notification."""
        item = self[index]
        print("Popped {} from the list.".format(item))
        return super().pop(index)
