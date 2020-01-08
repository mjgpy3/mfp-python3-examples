#!/usr/bin/env python3

from grid import Grid
from page105_polar_cell import PolarCell
from PIL import Image, ImageDraw
from math import pi, sin, cos
from random import randrange

class PolarGrid(Grid):
  def __init__(self, rows):
    Grid.__init__(self, rows, 1)

  def prepare_grid(self):
    rows = list(range(self.rows))

    row_height = 1.0 / self.rows
    rows[0] = [ PolarCell(0, 0) ]

    for row in range(1, self.rows):
      radius = float(row) / self.rows
      circumference = 2 * pi * radius

      previous_count = len(rows[row-1])
      estimated_cell_width = circumference / previous_count
      ratio = round(estimated_cell_width / row_height)

      cells = previous_count * ratio
      rows[row] = [PolarCell(row, col) for col in range(cells)]

    return rows

  def configure_cells(self):
    for cell in self.each_cell():
      row, col = cell.row, cell.column

      if row > 0:
        cell.cw = self[(row, col+1)]
        cell.ccw = self[(row, col-1)]

        ratio = len(self.grid[row]) // len(self.grid[row - 1])
        parent = self.grid[row - 1][col // ratio]
        parent.outward.append(cell)
        cell.inward = parent

  def __getitem__(self, row_col):
    row = row_col[0]
    column = row_col[1]

    if row < 0 or row >= self.rows:
      return None

    return self.grid[row][column % len(self.grid[row])]

  def random_cell(self):
    row = randrange(0, self.rows)
    col = randrange(0, len(self.grid[row]))
    return self.grid[row][col]

  # This library (PIL) is actually far more robust than just PNGs but we'll keep it
  # named that for now...
  def to_png(self, cell_size = 10):
    img_size = 2 * self.rows * cell_size

    background = (255,255,255)
    wall = (0,0,0)

    img = Image.new('RGB', size=(img_size+1, img_size+1), color=background)
    draw = ImageDraw.Draw(img)
    center = img_size // 2

    for cell in self.each_cell():
      if cell.row == 0:
        continue

      theta = 2 * pi / len(self.grid[cell.row])
      inner_radius = cell.row * cell_size
      outer_radius = (cell.row + 1) * cell_size
      theta_ccw = cell.column * theta
      theta_cw = (cell.column + 1) * theta

      ax = int(center + (inner_radius * cos(theta_ccw)))
      ay = int(center + (inner_radius * sin(theta_ccw)))
      bx = int(center + (outer_radius * cos(theta_ccw)))
      by = int(center + (outer_radius * sin(theta_ccw)))
      cx = int(center + (inner_radius * cos(theta_cw)))
      cy = int(center + (inner_radius * sin(theta_cw)))
      dx = int(center + (outer_radius * cos(theta_cw)))
      dy = int(center + (outer_radius * sin(theta_cw)))

      if not cell.is_linked(cell.inward):
        draw.line([(ax, ay), (cx, cy)], fill=wall)

      if not cell.is_linked(cell.cw):
        draw.line([(cx, cy), (dx, dy)], fill=wall)

    draw.arc([(0, 0), (self.rows*cell_size*2, self.rows*cell_size*2)], 0, 360, fill=wall)

    return img
