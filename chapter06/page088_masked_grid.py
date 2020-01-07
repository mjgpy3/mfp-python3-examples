#!/usr/bin/env python3

from grid import Grid
from cell import Cell

class MaskedGrid(Grid):
  def __init__(self, mask):
    self.mask = mask
    Grid.__init__(self, self.mask.rows, self.mask.columns)

  def prepare_grid(self):
    grid = []

    for row in range(self.rows):
      grid.append([])
      for column in range(self.columns):
        if self.mask[(row, column)]:
          grid[row].append(Cell(row, column))
        else:
          grid[row].append(None)

    return grid

  def random_cell(self):
    row, col = self.mask.random_location()

    return self[(row, col)]

  def __len__(self):
    return len(self.mask)
