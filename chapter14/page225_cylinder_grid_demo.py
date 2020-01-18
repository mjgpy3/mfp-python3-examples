#!/usr/bin/env python3

from page225_cylinder_grid import CylinderGrid
from recursive_backtracker import RecursiveBacktracker

grid = CylinderGrid(7, 16)
RecursiveBacktracker.on(grid)

filename = 'cylinder.png'
grid.to_png().save(filename)
print('saved to', filename)
