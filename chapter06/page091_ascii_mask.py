#!/usr/bin/env python3

from page087_mask import Mask
from page088_masked_grid import MaskedGrid
from recursive_backtracker import RecursiveBacktracker
import sys

if len(sys.argv) != 2:
  raise Exception('Please specify a text file to use as a template')
mask = Mask.from_txt(sys.argv[1])
grid = MaskedGrid(mask)
RecursiveBacktracker.on(grid)

filename = 'masked.png'
grid.write_png(filename)
print('saved image to', filename)
