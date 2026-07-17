#!/usr/bin/python3
"""Rotate 2D Matrix module."""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): n x n 2D matrix to rotate.

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
