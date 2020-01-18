#!/usr/bin/env python3

from cell import Cell
from grid import Grid
from random import choice
from PIL import Image, ImageDraw

class Cell3D(Cell):
  def __init__(self, level, row, column):
    self.level = level
    self.up = None
    self.down = None
    Cell.__init__(self, row, column)

  def neighbors(self):
    list = super().neighbors()
    if self.up:
      list.append(self.up)

    if self.down:
      list.append(self.down)

    return list

class Grid3D(Grid):
  def __init__(self, levels, rows, columns):
    self.levels = levels
    Grid.__init__(self, rows, columns)

  def prepare_grid(self):
    levels = []

    for level in range(self.levels):
      l = []
      levels.append(l)
      for row in range(self.rows):
        r = []
        l.append(r)
        for column in range(self.columns):
          r.append(Cell3D(level, row, column))

    return levels

  def configure_cells(self):
    for cell in self.each_cell():
      level, row, col = cell.level, cell.row, cell.column

      cell.north = self[(level, row - 1, col)]
      cell.south = self[(level, row + 1, col)]
      cell.west  = self[(level, row, col - 1)]
      cell.east  = self[(level, row, col + 1)]
      cell.down  = self[(level - 1, row, col)]
      cell.up    = self[(level + 1, row, col)]

  def __getitem__(self, level_row_col):
    level = level_row_col[0]
    row = level_row_col[1]
    column = level_row_col[2]

    if level < 0 or level >= self.levels:
      return None
    if row < 0 or row >= len(self.grid[level]):
      return None
    if column < 0 or column >= len(self.grid[level][row]):
      return None

    return self.grid[level][row][column]

  def random_cell(self):
    return choice(choice(choice(self.grid)))

  def __len__(self):
    return self.levels * self.rows * self.columns

  def each_level(self):
    for level in self.grid:
      yield level

  def each_row(self):
    for rows in self.each_level():
      for row in rows:
        yield row

  def to_png(self, cell_size = 10, inset = 0, margin=None):
    if not margin:
      margin = cell_size/2

    inset = int(cell_size * inset)

    grid_width = cell_size * self.columns
    grid_height = cell_size * self.rows

    img_width = int(grid_width * self.levels + (self.levels - 1) * margin)
    img_height = int(grid_height)

    background = (255, 255, 255)
    wall = (0, 0, 0)
    arrow = (255, 0, 0)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    for mode in ['backgrounds', 'walls']:
      for cell in self.each_cell():
        x = cell.level * (grid_width + margin) + cell.column * cell_size
        y = cell.row * cell_size

        if inset > 0:
          self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
        else:
          self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

        if mode == 'walls':
          mid_x = x + cell_size / 2
          mid_y = y + cell_size / 2

          if cell.is_linked(cell.down):
            draw.line([(mid_x-3, mid_y), (mid_x-1, mid_y+2)], fill=arrow)
            draw.line([(mid_x-3, mid_y), (mid_x-1, mid_y-2)], fill=arrow)

          if cell.is_linked(cell.up):
            draw.line([(mid_x+3, mid_y), (mid_x+1, mid_y+2)], fill=arrow)
            draw.line([(mid_x+3, mid_y), (mid_x+1, mid_y-2)], fill=arrow)

    return img
