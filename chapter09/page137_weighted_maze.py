#!/usr/bin/env python3

from page136_weighted_grid import WeightedGrid
from recursive_backtracker import RecursiveBacktracker

grid = WeightedGrid(10, 10)
RecursiveBacktracker.on(grid)

grid.braid(0.5)

start, finish = grid[(0, 0)], grid[(grid.rows-1, grid.columns-1)]

print(start, finish)

grid.set_distances(start.distances().path_to(finish))
filename = 'original.png'
grid.write_png(filename)
print('saved to', filename)
