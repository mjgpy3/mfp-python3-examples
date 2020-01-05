#!/usr/bin/env python3

from page041_binary_tree import BinaryTree
from page041_distance_grid import DistanceGrid

grid = DistanceGrid(10, 10)

BinaryTree.on(grid)

start = grid[(0, 0)]

distances = start.distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distance = new_distances.max()

grid.distances = new_distances.path_to(goal)
print(grid)
