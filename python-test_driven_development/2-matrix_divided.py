#!/usr/bin/python3
"""This module contains a function that divides all matrix elements"""


def matrix_divided(matrix, div):
    """Returns a new matrix with all values divided by div."""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])

    new_matrix = []

    for row in matrix:

        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        new_row = []

        for element in row:

            if type(element) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )

            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
