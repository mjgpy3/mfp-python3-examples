#!/usr/bin/env python3

from grid import Grid
from page122_triangle_cell import TriangleCell
from PIL import Image, ImageDraw
import math

class TriangleGrid(Grid):
  def prepare_grid(self):
    return [[TriangleCell(row, column) for column in range(self.columns)] for row in range(self.rows)]

  def configure_cells(self):
    for cell in self.each_cell():
      row, col = cell.row, cell.column

      cell.west = self[(row, col - 1)]
      cell.east = self[(row, col + 1)]

      if cell.is_upright():
        cell.south = self[(row + 1, col)]
      else:
        cell.north = self[(row - 1, col)]

  def to_png(self, size = 16):
    half_width = size / 2.0
    height = size * math.sqrt(3) / 2.0
    half_height = height / 2

    img_width = int(size * (self.columns + 1) / 2.0)
    img_height = int(height * self.rows)

    background = (255,255,255)
    wall = (0,0,0)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    for mode in ['backgrounds', 'walls']:
      for cell in self.each_cell():
        cx = half_width + cell.column * half_width
        cy = half_height + cell.row * height

        west_x = int(cx - half_width)
        mid_x = int(cx)
        east_x = int(cx + half_width)

        if cell.is_upright():
          apex_y = int(cy - half_height)
          base_y = int(cy + half_height)
        else:
          apex_y = int(cy + half_height)
          base_y = int(cy - half_height)

        if mode == 'backgrounds':
          color = self.background_color_for(cell)
          if color:
            points = [(west_x, base_y), (mid_x, apex_y), (east_x, base_y)]
            draw.polygon(points, fill=color, outline=color)
        else:
          if not cell.west:
            draw.line([(west_x, base_y), (mid_x, apex_y)], fill=wall)

          if not cell.is_linked(cell.east):
            draw.line([(east_x, base_y), (mid_x, apex_y)], fill=wall)

          no_south = cell.is_upright() and not cell.south
          not_linked = not cell.is_upright() and not cell.is_linked(cell.north)

          if no_south or not_linked:
            draw.line([(east_x, base_y), (west_x, base_y)], fill=wall)

    return img
