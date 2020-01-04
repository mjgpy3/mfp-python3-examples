#!/usr/bin/env python3

from page020_030 import Grid
from page028 import SideWinder

grid = Grid(4, 4)
SideWinder.on(grid)

grid.write_png('sidewinder.png', 20)
