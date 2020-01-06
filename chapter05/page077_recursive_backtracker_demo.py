#!/usr/bin/env python3

from page076_recursive_backtracker import RecursiveBacktracker 
from grid import Grid

grid = Grid(20, 20)
RecursiveBacktracker.on(grid)

filename = 'recursive_backtracker.png'
grid.write_png(filename)
print('saved to', filename)
