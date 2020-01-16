#!/usr/bin/env python3

from random import choice, randrange

class SimplifiedPrims:
  @staticmethod
  def on(grid, start_at = None):
    if not start_at:
      start_at = grid.random_cell()

    active = []
    active.append(start_at)

    while active:
      cell = choice(active)

      available_neighbors = [n for n in cell.neighbors() if not n.links]

      if available_neighbors:
        neighbor = choice(available_neighbors)
        cell.link(neighbor)
        active.append(neighbor)
      else:
        active.remove(cell)

    return grid

class TruePrims:
  @staticmethod
  def on(grid, start_at = None):
    if not start_at:
      start_at = grid.random_cell()

    active = []
    active.append(start_at)

    costs = {}
    for cell in grid.each_cell():
      costs[cell] = randrange(100)

    while active:
      cell = min(active, key=lambda c: costs[c])

      available_neighbors = [n for n in cell.neighbors() if not n.links]

      if available_neighbors:
        neighbor = min(available_neighbors, key=lambda n: costs[n])
        cell.link(neighbor)
        active.append(neighbor)
      else:
        active.remove(cell)

    return grid
