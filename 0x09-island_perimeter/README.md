# Island Perimeter Calculator

This project implements a function `island_perimeter` that calculates the perimeter of an island represented in a 2D grid.

## Project Description

The function determines the perimeter of an island in a grid where:
- `0` represents water.
- `1` represents land.

### Key Assumptions
- Each cell is square with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or none).
- The island does not have lakes (water completely surrounded by land).

## Requirements

- Python version: `3.4.3` or later
- OS: Ubuntu 20.04 LTS

## Files

- **`0-island_perimeter.py`**: Contains the implementation of the `island_perimeter` function.
- **`README.md`**: Provides details about the project.
