#!/usr/bin/env python3

from page057_grid import Grid
from page063_wilsons import Wilsons

grid = Grid(20, 20)
Wilsons.on(grid)

filename = 'wilsons.png'
grid.write_png(filename)
print('saved to', filename)
