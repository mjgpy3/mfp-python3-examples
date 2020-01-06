#!/usr/bin/env python3

from random import choice

class AldousBroder:
  @staticmethod
  def on(grid):
    cell = grid.random_cell()
    unvisited = len(grid) - 1

    while unvisited > 0:
      neighbor = choice(cell.neighbors())

      if not neighbor.links:
        cell.link(neighbor)
        unvisited -= 1

      cell = neighbor

    return grid
