#!/usr/bin/env python3

from page214_grid3d import Grid3D
from recursive_backtracker import RecursiveBacktracker

grid = Grid3D(3, 3, 3)
RecursiveBacktracker.on(grid)

filename = '3d.png'
grid.to_png(cell_size=20).save(filename)
print('saved to', filename)
