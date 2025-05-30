#!/usr/bin/python3
"""Implements a function to divide elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The number to divide by.
    Raises:
        TypeError: If any element in the matrix is not a number.
        TypeError: If the rows in the matrix are of different lengths.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    Returns:
        A new matrix containing the results of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
