#!/usr/bin/python3
"""This module defines shape classes."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def perimeter(self):
        """Return shape perimeter."""
        pass

    @abstractmethod
    def area(self):
        """Return shape area."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialises circle."""
        self.radius = radius

    def area(self):
        """Return circle area."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialises rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape area and perimeter."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
