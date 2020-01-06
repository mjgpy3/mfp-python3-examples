#!/usr/bin/env python3

from random import choice

class Wilsons:
  @staticmethod
  def on(grid):
    unvisited = list(grid.each_cell())

    first = choice(unvisited)
    unvisited.remove(first)

    while unvisited:
      cell = choice(unvisited)
      path = [cell]

      while cell in unvisited:
        cell = choice(cell.neighbors())
        try:
          position = path.index(cell)
          path = path[:position+1]
        except ValueError:
          path.append(cell)

      for index in range(len(path)-1):
        path[index].link(path[index + 1])
        unvisited.remove(path[index])

    return grid
