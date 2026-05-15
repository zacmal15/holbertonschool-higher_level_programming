#!/usr/bin/python3


def print_square(size):
    """Prints a square using the # character."""

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)
