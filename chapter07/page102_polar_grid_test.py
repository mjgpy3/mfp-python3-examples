#!/usr/bin/env python3

from page101_polar_grid import PolarGrid

# Modified later to take 1 argument.
grid = PolarGrid(8)
filename = 'polar.png'
grid.to_png(cell_size=20).save(filename, 'PNG')
print('saved to', filename)
