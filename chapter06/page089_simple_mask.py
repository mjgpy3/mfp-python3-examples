#!/usr/bin/env python3

from page087_mask import Mask
from page088_masked_grid import MaskedGrid
from recursive_backtracker import RecursiveBacktracker

mask = Mask(5, 5)

mask[(0, 0)] = False
mask[(2, 2)] = False
mask[(4, 4)] = False

grid = MaskedGrid(mask)
RecursiveBacktracker.on(grid)
print(grid)
