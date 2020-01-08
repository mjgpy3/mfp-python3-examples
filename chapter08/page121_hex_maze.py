#!/usr/bin/env python3

from recursive_backtracker import RecursiveBacktracker
from page116_hex_grid import HexGrid

grid = HexGrid(10, 10)
RecursiveBacktracker.on(grid)

grid.to_png().save('hex.png')
