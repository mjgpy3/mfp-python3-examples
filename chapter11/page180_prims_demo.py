#!/usr/bin/env python3

from page179_prims import SimplifiedPrims
from grid import Grid

grid = Grid(20, 20)
SimplifiedPrims.on(grid)

filename = 'prims-simple.png'
grid.to_png().save(filename)
print('saved to', filename)
