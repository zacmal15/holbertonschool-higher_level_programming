#!/usr/bin/python3
"""Unittest for the max_integer function."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer."""

    def test_ordered_list(self):
        """Test a list already in order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list not in order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 8, -2]), 8)

    def test_max_at_beginning(self):
        """Test when the max number is first."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_repeated_max(self):
        """Test repeated maximum values."""
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)


if __name__ == "__main__":
    unittest.main()