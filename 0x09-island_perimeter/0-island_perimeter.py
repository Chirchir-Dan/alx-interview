#!/usr/bin/python3
"""
Island Perimeter Module

This module provides a function to calculate the perimeter of an island represented
in a 2D grid. The grid is a rectangular list of lists where:
- 0 represents water
- 1 represents land

The function adheres to the following assumptions:
- Each cell is square with a side length of 1.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is completely surrounded by water.
- There is only one island (or none).
- The island does not have lakes (water completely surrounded by land).
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 0
        represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 sides for the land cell
                perimeter += 4

                # Check if the cell above is land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check if the cell to the left is land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
