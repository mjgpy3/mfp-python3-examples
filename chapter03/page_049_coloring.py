#!/usr/bin/env python3

from page048_colored_grid import ColoredGrid
from page041_binary_tree import BinaryTree

grid = ColoredGrid(25, 25)
BinaryTree.on(grid)

start = grid[(grid.rows // 2, grid.columns // 2)]

grid.set_distances(start.distances())

filename = 'colorized.png'
grid.write_png(filename)
print('saved to', filename)
