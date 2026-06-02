#!/usr/bin/python3
"""This module defines a Student class."""


class Student:
    """This class represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with a first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if type(attrs) is list:
            new_dict = {}

            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]

            return new_dict

        return self.__dict__