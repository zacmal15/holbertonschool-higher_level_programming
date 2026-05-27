#!/usr/bin/python3
"""This module defines abstract Animal classes."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the animal sound."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
