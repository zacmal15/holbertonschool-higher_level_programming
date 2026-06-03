#!/usr/bin/python3

import pickle


class CustomObject:
    """Custom object class."""

    def __init__(self, name, age, is_student):
        """Initialises object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialise object into a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
