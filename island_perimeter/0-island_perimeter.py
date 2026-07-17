#!/usr/bin/python3
"""Island Perimeter module."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Args:
        grid (list): list of list of integers where 0 is water
            and 1 is land.

    Returns:
        The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
