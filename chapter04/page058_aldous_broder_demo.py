#!/usr/bin/env python3

from page057_aldous_broder import AldousBroder
from page057_grid import Grid

grid = Grid(20, 20)
AldousBroder.on(grid)

filename = 'aldous_broder.png'
grid.write_png(filename)
print('saved to', filename)
