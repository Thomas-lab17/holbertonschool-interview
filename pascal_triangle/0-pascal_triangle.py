#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list[list[int]]: Pascal's triangle of size n.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = (
                triangle[i - 1][j - 1] + triangle[i - 1][j]
            )
        triangle.append(row)
    return triangle
