#!/usr/bin/env python3

from page164_kruskals import Kruskals
from grid import Grid

grid = Grid(20, 20)
Kruskals.on(grid)

filename = 'kruskals.png'
grid.to_png().save(filename)
print('saved to', filename)
