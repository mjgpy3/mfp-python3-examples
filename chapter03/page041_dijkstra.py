#!/usr/bin/env python3

from page041_binary_tree import BinaryTree
from page041_distance_grid import DistanceGrid

grid = DistanceGrid(5, 5)

BinaryTree.on(grid)

start = grid[(0, 0)]

distances = start.distances()

grid.distances = distances

print(grid)

grid.distances = distances.path_to(grid[(grid.rows - 1, 0)])

print(grid)
