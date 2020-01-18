#!/usr/bin/env python3

from page225_cylinder_grid import CylinderGrid
from PIL import Image, ImageDraw

class MoebiusGrid(CylinderGrid):
  def __init__(self, rows, columns):
    CylinderGrid.__init__(self, rows, columns*2)

  def to_png(self, cell_size = 10, inset = 0):
    grid_height = cell_size * self.rows
    mid_point = self.columns // 2

    img_width = cell_size * mid_point
    img_height = grid_height * 2

    inset = int(cell_size * inset)

    background = (255, 255, 255)
    wall = (0, 0, 0)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    for mode in ['backgrounds', 'walls']:
      for cell in self.each_cell():
        x = (cell.column % mid_point) * cell_size
        y = cell.row * cell_size

        if cell.column > mid_point:
          y += grid_height

        if inset > 0:
          self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
        else:
          self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

    return img
