#!/usr/bin/python3
"""This module contains a function that prints formatted text."""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):

        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")

            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1

        i += 1
