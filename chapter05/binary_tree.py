#!/usr/bin/env python3

from random import choice

class BinaryTree:
  @staticmethod
  def on(grid):
    for cell in grid.each_cell():
      neighbors = []
      if cell.north:
        neighbors.append(cell.north)
      if cell.east:
        neighbors.append(cell.east)

      if neighbors:
        neighbor = choice(neighbors)
        cell.link(neighbor)

    return grid
