#!/usr/bin/env python3

from page101_polar_grid import PolarGrid
from recursive_backtracker import RecursiveBacktracker

grid = PolarGrid(80)
RecursiveBacktracker.on(grid)

filename = 'cirle_maze.png'
grid.to_png(cell_size=10).save(filename, 'PNG')
print('saved to', filename)
