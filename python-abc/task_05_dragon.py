#!/usr/bin/python3
"""This module defines mixin classes."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Print flying message."""
        print("The creaturen flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class using mixins."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
