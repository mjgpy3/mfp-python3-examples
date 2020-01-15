#!/usr/bin/env python3

from recursive_backtracker import RecursiveBacktracker
from page149_weave_grid import WeaveGrid

grid = WeaveGrid(20, 20)
RecursiveBacktracker.on(grid)

filename = 'weave.png'
grid.to_png().save(filename)
print('saved to', filename)
