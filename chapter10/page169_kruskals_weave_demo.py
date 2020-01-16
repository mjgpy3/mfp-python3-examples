#!/usr/bin/env python3

from random import randrange
from page164_kruskals import Kruskals
from weave_grid import WeaveGrid
from weave_cells import OverCell

class SimpleOverCell(OverCell):
  def neighbors(self):
    list = []
    if self.north:
      list.append(self.north)
    if self.south:
      list.append(self.south)
    if self.east:
      list.append(self.east)
    if self.west:
      list.append(self.west)
    return list

class PreconfiguredGrid(WeaveGrid):
  def prepare_grid(self):
    return [[SimpleOverCell(row, column, self) for column in range(self.columns)] for row in range(self.rows)]

grid = PreconfiguredGrid(20, 20)
state = Kruskals.State(grid)

for _ in range(len(grid)):
  row = 1 + randrange(grid.rows - 2)
  column = 1 + randrange(grid.columns - 2)
  state.add_crossing(grid[(row, column)])

Kruskals.on(grid, state)

filename = 'weave_kruskals.png'
grid.to_png(cell_size = 10, inset = 0.2).save(filename)
print('saved to', filename)
