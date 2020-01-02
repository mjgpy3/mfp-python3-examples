#!/usr/bin/env python3

from page018_020 import *

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
