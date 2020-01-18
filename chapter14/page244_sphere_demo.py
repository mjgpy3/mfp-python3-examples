#!/usr/bin/env python3

from page238_sphere_grid import SphereGrid
from recursive_backtracker import RecursiveBacktracker

grid = SphereGrid(20)
RecursiveBacktracker.on(grid)

filename = 'sphere-map.png'
grid.to_png().save(filename)
print('saved to', filename)
