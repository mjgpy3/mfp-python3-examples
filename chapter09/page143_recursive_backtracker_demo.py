#!/usr/bin/env python3

from recursive_backtracker import RecursiveBacktracker 
from grid import Grid

grid = Grid(20, 20)
RecursiveBacktracker.on(grid)

filename = 'inset.png'
grid.to_png(cell_size = 10, inset = 0.1).save('inset.png')
print('saved to', filename)
