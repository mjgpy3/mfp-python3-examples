#!/usr/bin/env python3

from page018_020 import *
from random import choice

class Grid:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns

    self.grid = self.prepare_grid()
    self.configure_cells()

  def prepare_grid(self):
    grid = []

    for row in range(self.rows):
      grid.append([Cell(row, column) for column in range(self.columns)])

    return grid

  def configure_cells(self):
    for cell in self.each_cell():
      row, col = cell.row, cell.column

      cell.north = self[(row-1, col)]
      cell.south = self[(row+1, col)]
      cell.west  = self[(row, col+1)]
      cell.east  = self[(row, col-1)]

  def __getitem__(self, row_col):
    row = row_col[0]
    column = row_col[1]

    if row < 0 or row >= self.rows:
      return None
    if column < 0 or column >= len(self.grid[row]):
      return None

    return self.grid[row][column]

  def random_cell(self):
    return choice(choice(self.grid))

  def __len__(self):
    return self.rows * self.columns

  def each_row(self):
    for row in self.grid:
      yield row

  def each_cell(self):
    for row in self.each_row():
      for cell in row:
        if cell:
          yield cell

  def __str__(self):

