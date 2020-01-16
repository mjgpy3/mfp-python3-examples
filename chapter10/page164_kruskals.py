#!/usr/bin/env python3

from random import shuffle, choice

class Kruskals:
  class State:
    def __init__(self, grid):
      self.grid = grid
      self.neighbors = []
      self.set_for_cell = {}
      self.cells_in_set = {}

      for cell in grid.each_cell():
        set = len(self.set_for_cell)

        self.set_for_cell[cell] = set
        self.cells_in_set[set] = [ cell ]

        if cell.south:
          self.neighbors.append((cell, cell.south))

        if cell.east:
          self.neighbors.append((cell, cell.east))

    def can_merge(self, left, right):
      return self.set_for_cell[left] != self.set_for_cell[right]

    def merge(self, left, right):
      left.link(right)

      winner = self.set_for_cell[left]
      loser = self.set_for_cell.get(right, None)
      losers = self.cells_in_set.get(loser, [right])

      for cell in losers:
        self.cells_in_set[winner].append(cell)
        self.set_for_cell[cell] = winner

      if loser in self.cells_in_set:
        del self.cells_in_set[loser]

    def add_crossing(self, cell):
      if (cell.links or
          not self.can_merge(cell.east, cell.west) or
          not self.can_merge(cell.north, cell.south)):
        return False

      self.neighbors = [(left, right) for (left, right) in self.neighbors if not (left == cell or right == cell)]

      if choice([True, False]):
        self.merge(cell.west, cell)
        self.merge(cell, cell.east)

        self.grid.tunnel_under(cell)
        self.merge(cell.north, cell.north.south)
        self.merge(cell.south, cell.south.north)
      else:
        self.merge(cell.north, cell)
        self.merge(cell, cell.south)

        self.grid.tunnel_under(cell)
        self.merge(cell.west, cell.west.east)
        self.merge(cell.east, cell.east.west)

  @staticmethod
  def on(grid, state=None):
    if not state:
      state = Kruskals.State(grid)

   
    neighbors = state.neighbors
    shuffle(neighbors)

    while neighbors:
      left, right = neighbors.pop()
      if state.can_merge(left, right):
        state.merge(left, right)

    return grid
