#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialises a square with a size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current square area."""

        return self.__size * self.__size
