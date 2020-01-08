#!/usr/bin/env python3

from random import choice

class RecursiveBacktracker:
  @staticmethod
  def on(grid, start_at = None):
    if start_at == None:
      start_at = grid.random_cell()

    stack = []
    stack.append(start_at)

    while stack:
      current = stack[-1]
      neighbors = [n for n in current.neighbors() if not n.links]

      if not neighbors:
        stack.pop()
      else:
        neighbor = choice(neighbors)
        current.link(neighbor)
        stack.append(neighbor)

    return grid
