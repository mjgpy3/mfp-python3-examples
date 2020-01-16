#!/usr/bin/env python3

from page184_growing_tree import GrowingTree
from grid import Grid
from random import choice

def save(grid, filename):
  grid.to_png().save(filename)
  print('saved to', filename)

grid = Grid(20, 20)
GrowingTree.on(grid, choice)
save(grid, 'growing-tree-random.png')

grid = Grid(20, 20)
GrowingTree.on(grid, lambda list: list[-1])
save(grid, 'growing-tree-last.png')

grid = Grid(20, 20)
GrowingTree.on(grid, lambda list: list[-1] if choice([True, False]) else choice(list))
save(grid, 'growing-tree-mix.png')
