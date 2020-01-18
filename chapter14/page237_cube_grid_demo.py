#!/usr/bin/env python3

from page230_cube_grid import CubeGrid
from recursive_backtracker import RecursiveBacktracker

grid = CubeGrid(10)
RecursiveBacktracker.on(grid)

filename = 'cube.png'
grid.to_png().save(filename)
print('saved to', filename)
