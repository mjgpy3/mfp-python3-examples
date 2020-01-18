#!/usr/bin/env python3

from random import choice, shuffle, randrange

class Ellers:
  class RowState:
    def __init__(self, starting_set=0):
      self.cells_in_set = {}
      # Dict<int, *> in python kind of behaves like array in ruby... Odd.
      self.set_for_cell = {}
      self.next_set = starting_set

    def record(self, set, cell):
      self.set_for_cell[cell.column] = set

      if set not in self.cells_in_set:
        self.cells_in_set[set] = []

      self.cells_in_set[set].append(cell)

    def set_for(self, cell):
      if cell.column not in self.set_for_cell:
        self.record(self.next_set, cell)
        self.next_set += 1

      return self.set_for_cell[cell.column]

    def merge(self, winner, loser):
      for cell in self.cells_in_set[loser]:
        self.set_for_cell[cell.column] = winner
        self.cells_in_set[winner].append(cell)

      del self.cells_in_set[loser]

    def next(self):
      return Ellers.RowState(self.next_set)

    def each_set(self):
      return [(set, self.cells_in_set[set]) for set in self.cells_in_set]


  @staticmethod
  def on(grid):
    row_state = Ellers.RowState()

    for row in grid.each_row():
      for cell in row:
        if not cell.west:
          continue

        set = row_state.set_for(cell)
        prior_set = row_state.set_for(cell.west)

        should_link = set != prior_set and (not cell.south or choice([True, False]))

        if should_link:
          cell.link(cell.west)
          row_state.merge(prior_set, set)

      if row[0].south:
        next_row = row_state.next()

        for (set, list) in row_state.each_set():
          list2 = list[:]
          shuffle(list2)
          for (index, cell) in enumerate(list2):
            if index == 0 or randrange(3) == 0:
              cell.link(cell.south)
              next_row.record(row_state.set_for(cell), cell.south)

        row_state = next_row
