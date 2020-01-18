#!/usr/bin/env python3

from page200_recursive_division import RecursiveDivision
from grid import Grid

grid = Grid(20, 20)
RecursiveDivision.on(grid)

filename = 'recursive_division.png'
grid.to_png().save(filename)
print('saved to', filename)
