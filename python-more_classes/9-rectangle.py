#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """This class defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises a rectangle with width and height."""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable rectangle using # characters."""

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []

        for i in range(self.__height):
            rectangle.append(
                str(self.print_symbol) * self.__width
            )

        return "\n".join(rectangle)

    def __repr__(self):
        """Returns a string representation to recreate the object."""

        return "Rectangle({}, {})".format(
            self.__width,
            self.__height
        )

    def __del__(self):
        """Print a message when the rectangle is deleted."""

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the bigger area."""

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with equal sides."""

        return cls(size, size)
