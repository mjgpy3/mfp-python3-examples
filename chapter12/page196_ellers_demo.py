#!/usr/bin/env python3

from page193_ellers import Ellers
from grid import Grid

grid = Grid(20, 20)
Ellers.on(grid)

filename = 'ellers.png'
grid.to_png().save(filename)
print('saved to', filename)
