#!/usr/bin/env python3

from random import choice

class HuntAndKill:
  @staticmethod
  def on(grid):
    current = grid.random_cell()

    while current:
      unvisited_neighbors = [n for n in current.neighbors() if not n.links]

      if unvisited_neighbors:
        neighbor = choice(unvisited_neighbors)
        current.link(neighbor)
        current = neighbor
      else:
        current = None

        for cell in grid.each_cell():
          visited_neighbors = [n for n in cell.neighbors() if n.links]
          if not cell.links and visited_neighbors:
            current = cell
            neighbor = choice(visited_neighbors)
            current.link(neighbor)

            break

    return grid
