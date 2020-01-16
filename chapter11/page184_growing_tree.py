#!/usr/bin/env python3

from random import choice

class GrowingTree:
  @staticmethod
  def on(grid, cell_from_active, start_at = None):
    if not start_at:
      start_at = grid.random_cell()

    active = []
    active.append(start_at)

    while active:
      cell = cell_from_active(active)

      available_neighbors = [n for n in cell.neighbors() if not n.links]

      if available_neighbors:
        neighbor = choice(available_neighbors)
        cell.link(neighbor)
        active.append(neighbor)
      else:
        active.remove(cell)

    return grid


