#!/usr/bin/env python3

from recursive_backtracker import RecursiveBacktracker
from page123_triangle_grid import TriangleGrid

grid = TriangleGrid(10, 17)
RecursiveBacktracker.on(grid)

grid.to_png().save('delta.png')
