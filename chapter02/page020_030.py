#!/usr/bin/env python3

from page018_020 import *
from random import choice
import png

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
      cell.west  = self[(row, col-1)]
      cell.east  = self[(row, col+1)]

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
    output = '+' + self.columns*'---+' + '\n'

    for row in self.each_row():
      top = '|'
      bottom = '+'

      for cell in row:
        if not cell:
          cell = Cell(-1, -1)

        body = '   '
        if cell.is_linked(cell.east):
          east_boundary = ' '
        else:
          east_boundary = '|'

        top = top + body + east_boundary

        if cell.is_linked(cell.south):
          south_boundary = '   '
        else:
          south_boundary = '---'

        corner = '+'
        bottom = bottom + south_boundary + corner

      output = output + top + '\n'
      output = output + bottom + '\n'

    return output

  def write_png(self, file_name, cell_size = 10):
    s = self.to_png_bits(cell_size)

    w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
    with open(file_name, 'wb') as f:
      w.write(f, s)

  # Really more of an adapted `__str__` than the book's example since the
  # `pypng` interface doesn't have `line` a la ChunkyPNG
  def to_png_bits(self, cell_size = 10):
    black = 0
    white = 1

    output = [self.columns * cell_size * [black] + [black]]

    for row in self.each_row():
      top = [black]
      bottom = [black]

      for cell in row:
        if not cell:
          cell = Cell(-1, -1)

        body = (cell_size-1) * [white]
        if cell.is_linked(cell.east):
          east_boundary = [white]
        else:
          east_boundary = [black]

        top = top + body + east_boundary

        if cell.is_linked(cell.south):
          south_boundary = (cell_size-1) * [white]
        else:
          south_boundary = (cell_size-1) * [black]

        corner = [black]
        bottom = bottom + south_boundary + corner

      for _ in range(cell_size):
        output.append(top)
      output.append(bottom)

    return output
