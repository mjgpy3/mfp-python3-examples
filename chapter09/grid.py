#!/usr/bin/env python3

from cell import *
from random import choice, shuffle, random
from PIL import Image, ImageDraw

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

  def contents_of(self, cell):
    return ' '

  def __str__(self):
    output = '+' + self.columns*'---+' + '\n'

    for row in self.each_row():
      top = '|'
      bottom = '+'

      for cell in row:
        if not cell:
          cell = Cell(-1, -1)

        body = ' ' + self.contents_of(cell) + ' '
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

  def background_color_for(self, cell):
    return (255, 255, 255)

  def to_png(self, cell_size = 10, inset = 0):
    img_width = cell_size * self.columns
    img_height = cell_size * self.rows
    inset = int(cell_size * inset)

    background = (255, 255, 255)
    wall = (0, 0, 0)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    for mode in ['backgrounds', 'walls']:
      for cell in self.each_cell():
        x = cell.column * cell_size
        y = cell.row * cell_size

        if inset > 0:
          self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
        else:
          self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

    return img

  def to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y):
    x1, y1 = x, y
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    if mode == 'backgrounds':
      color = self.background_color_for(cell)
      if color:
        draw.rectangle([x, y, x2, y2], fill=color, outline=color)
    else:
      if not cell.north:
        draw.line([(x1, y1), (x2, y1)], fill=wall)

      if not cell.west:
        draw.line([(x1, y1), (x1, y2)], fill=wall)

      if not cell.is_linked(cell.east):
        draw.line([(x2, y1), (x2, y2)], fill=wall)

      if not cell.is_linked(cell.south):
        draw.line([(x1, y2), (x2, y2)], fill=wall)

  def cell_coordinates_with_inset(self, x, y, cell_size, inset):
    x1, x4 = x, x + cell_size
    x2 = x1 + inset
    x3 = x4 - inset

    y1, y4 = y, y + cell_size
    y2 = y1 + inset
    y3 = y4 - inset

    return (x1, x2, x3, x4,
             y1, y2, y3, y4)

  def to_png_with_inset(self, draw, cell, mode, cell_size, wall, x, y, inset):
    x1, x2, x3, x4, y1, y2, y3, y4 = (
      self.cell_coordinates_with_inset(x, y, cell_size, inset)
    )

    if mode == 'backgrounds':
      pass
    else:
      if cell.is_linked(cell.north):
        draw.line([(x2, y1), (x2, y2)], fill=wall)
        draw.line([(x3, y1), (x3, y2)], fill=wall)
      else:
        draw.line([(x2, y2), (x3, y2)], fill=wall)

      if cell.is_linked(cell.south):
        draw.line([(x2, y3), (x2, y4)], fill=wall)
        draw.line([(x3, y3), (x3, y4)], fill=wall)
      else:
        draw.line([(x2, y3), (x3, y3)], fill=wall)

      if cell.is_linked(cell.west):
        draw.line([(x1, y2), (x2, y2)], fill=wall)
        draw.line([(x1, y3), (x2, y3)], fill=wall)
      else:
        draw.line([(x2, y2), (x2, y3)], fill=wall)

      if cell.is_linked(cell.east):
        draw.line([(x3, y2), (x4, y2)], fill=wall)
        draw.line([(x3, y3), (x4, y3)], fill=wall)
      else:
        draw.line([(x3, y2), (x3, y3)], fill=wall)

  def deadends(self):
    return [cell for cell in self.each_cell() if len(cell.links) == 1]

  def braid(self, p = 1.0):
    deadends = self.deadends()
    shuffle(deadends)
    for cell in deadends:
      if len(cell.links) != 1 or random() > p:
        continue

      neighbors = [n for n in cell.neighbors() if not cell.is_linked(n)]
      best = [n for n in neighbors if len(n.links) == 1]
      if not best:
        best = neighbors

      neighbor = choice(best)
      cell.link(neighbor)

def flatten_list_of_tuples_to_tuple(lot):
  return tuple(v for t in lot for v in t)
