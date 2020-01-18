#!/usr/bin/env python3

from page227_moebius_grid import MoebiusGrid
from recursive_backtracker import RecursiveBacktracker

grid = MoebiusGrid(5, 50)
RecursiveBacktracker.on(grid)

filename = 'moebius.png'
grid.to_png().save(filename)
print('saved to', filename)
