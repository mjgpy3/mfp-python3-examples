#!/usr/bin/env python3

from grid import Grid
from page069_hunt_and_kill import HuntAndKill

grid = Grid(20, 20)
HuntAndKill.on(grid)

filename = 'hunt_and_kill.png'
grid.write_png(filename)
print('saved to', filename)
