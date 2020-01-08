#!/usr/bin/env python3

from grid import Grid
from page114_hex_cell import HexCell
from PIL import Image, ImageDraw
import math

class HexGrid(Grid):
  def prepare_grid(self):
    return [[HexCell(row, column) for column in range(self.columns)] for row in range(self.rows)]

  def configure_cells(self):
    for cell in self.each_cell():
      row, col = cell.row, cell.column

      if col % 2 == 0:
        north_diagonal = row - 1
        south_diagonal = row
      else:
        north_diagonal = row
        south_diagonal = row + 1

      cell.northwest = self[(north_diagonal, col - 1)]
      cell.north     = self[(row - 1, col)]
      cell.northeast = self[(north_diagonal, col + 1)]
      cell.southwest = self[(south_diagonal, col - 1)]
      cell.south     = self[(row + 1, col)]
      cell.southeast = self[(south_diagonal, col + 1)]

  def to_png(self, size = 10):
    a_size = size / 2.0
    b_size = size * math.sqrt(3) / 2.0
    width = size * 2
    height = b_size * 2

    img_width = int(3 * a_size * self.columns + a_size + 0.5)
    img_height = int(height * self.rows + b_size + 0.5)

    background = (255,255,255)
    wall = (0,0,0)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    for mode in ['backgrounds', 'walls']:
      for cell in self.each_cell():
        cx = size + 3 * cell.column * a_size
        cy = b_size + cell.row * height
        if cell.column % 2 != 0:
          cy += b_size

        # f/n = far/near
        # n/s/e/w = north/south/east/west
        x_fw = int(cx - size)
        x_nw = int(cx - a_size)
        x_ne = int(cx + a_size)
        x_fe = int(cx + size)

        # m = middle
        y_n = int(cy - b_size)
        y_m = int(cy)
        y_s = int(cy + b_size)

        if mode == 'backgrounds':
          color = self.background_color_for(cell)
          points =  [(x_fw, y_m), (x_nw, y_n), (x_ne, y_n),
                     (x_fe, y_m), (x_ne, y_s), (x_nw, y_s)]
          draw.polygon(points, fill=color, outline=color)
        else:
          if not cell.southwest:
            draw.line([(x_fw, y_m), (x_nw, y_s)], fill=wall)

          if not cell.northwest:
            draw.line([(x_fw, y_m), (x_nw, y_n)], fill=wall)

          if not cell.north:
            draw.line([(x_nw, y_n), (x_ne, y_n)], fill=wall)

          if not cell.is_linked(cell.northeast):
            draw.line([(x_ne, y_n), (x_fe, y_m)], fill=wall)

          if not cell.is_linked(cell.southeast):
            draw.line([(x_fe, y_m), (x_ne, y_s)], fill=wall)

          if not cell.is_linked(cell.south):
            draw.line([(x_ne, y_s), (x_nw, y_s)], fill=wall)

    return img

