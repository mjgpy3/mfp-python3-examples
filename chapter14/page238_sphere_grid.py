#!/usr/bin/env python3

from polar_cell import PolarCell
from polar_grid import PolarGrid
from grid import Grid
from math import pi, sin
from random import choice
from PIL import Image, ImageDraw

class HemisphereCell(PolarCell):
  def __init__(self, hemisphere, row, column):
    self.hemisphere = hemisphere
    PolarCell.__init__(self, row, column)

class HemisphereGrid(PolarGrid):
  def __init__(self, id, rows):
    self.id = id
    PolarGrid.__init__(self, rows)

  def size(self, row):
    return len(self.grid[row])

  def prepare_grid(self):
    grid = self.rows*[None]

    angular_height =  pi / (2 * self.rows)

    grid[0] = [HemisphereCell(self.id, 0, 0)]

    for row in range(1, self.rows):
      theta = (row + 1) * angular_height
      radius = sin(theta)
      circumference = 2 * pi * radius

      previous_count = len(grid[row - 1])
      estimated_cell_width = circumference / previous_count
      ratio = round(estimated_cell_width / angular_height)

      cells = previous_count * ratio
      grid[row] = [HemisphereCell(self.id, row, col) for col in range(cells)]

    return grid

class SphereGrid(Grid):
  def __init__(self, rows):
    assert rows % 2 == 0, 'argument must be an even number'

    self.equator = rows // 2
    Grid.__init__(self, rows, 1)

  def prepare_grid(self):
    return [HemisphereGrid(id, self.equator) for id in range(2)]

  def configure_cells(self):
    belt = self.equator - 1
    for index in range(belt):
      a, b = self[(0, belt, index)], self[(1, belt, index)]
      a.outward.append(b)
      b.outward.append(a)

  def __getitem__(self, hemi_row_col):
    hemi = hemi_row_col[0]
    row = hemi_row_col[1]
    column = hemi_row_col[2]

    return self.grid[hemi][(row, column)]

  def size(self, row):
    return self.grid[0].size(row)

  def each_cell(self):
    for hemi in self.grid:
      for cell in hemi.each_cell():
        yield cell

  def random_cell(self):
    return choice(self.grid).random_cell()

  def to_png(self, ideal_size = 10):
    img_height = ideal_size * self.rows
    img_width = self.grid[0].size(self.equator - 1) * ideal_size

    background = (255, 255, 255)
    wall = (0, 0, 0)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    for cell in self.each_cell():
      row_size = self.size(cell.row)
      cell_width = float(img_width) / row_size

      x1 = cell.column * cell_width
      x2 = x1 + cell_width

      y1 = cell.row * ideal_size
      y2 = y1 + ideal_size

      if cell.hemisphere > 0:
        y1 = img_height - y1
        y2 = img_height - y2

      x1 = round(x1); y1 = round(y1)
      x2 = round(x2); y2 = round(y2)

      if cell.row > 0:
        if not cell.is_linked(cell.cw):
          draw.line([(x2, y1), (x2, y2)], fill=wall)

        if not cell.is_linked(cell.inward):
          draw.line([(x1, y1), (x2, y1)], fill=wall)

      if cell.hemisphere == 0 and cell.row == self.equator - 1:
        if not cell.outward or not cell.is_linked(cell.outward[0]):
          draw.line([(x1, y2), (x2, y2)], fill=wall)

    return img
