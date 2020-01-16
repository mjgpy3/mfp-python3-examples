#!/usr/bin/env python3

from grid import Grid
from weave_cells import OverCell, UnderCell

class WeaveGrid(Grid):
  def __init__(self, rows, columns):
    self.under_cells = []
    Grid.__init__(self, rows, columns)

  def prepare_grid(self):
    return [[OverCell(row, column, self) for column in range(self.columns)] for row in range(self.rows)]

  def tunnel_under(self, over_cell):
    under_cell = UnderCell(over_cell)
    self.under_cells.append(under_cell)

  def each_cell(self):
    for cell in super().each_cell():
      yield cell

    for cell in self.under_cells:
      yield cell

  def to_png(self, cell_size = 10, inset = None):
    return super().to_png(cell_size, inset or 0.1)

  def to_png_with_inset(self, draw, cell, mode, cell_size, wall, x, y, inset):
    if isinstance(cell, OverCell):
      super().to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
    else:
      x1, x2, x3, x4, y1, y2, y3, y4 = (
        self.cell_coordinates_with_inset(x, y, cell_size, inset)
      )

      if cell.vertical_passage():
        draw.line([(x2, y1), (x2, y2)], fill=wall)
        draw.line([(x3, y1), (x3, y2)], fill=wall)
        draw.line([(x2, y3), (x2, y4)], fill=wall)
        draw.line([(x3, y3), (x3, y4)], fill=wall)
      else:
        draw.line([(x1, y2), (x2, y2)], fill=wall)
        draw.line([(x1, y3), (x2, y3)], fill=wall)
        draw.line([(x3, y2), (x4, y2)], fill=wall)
        draw.line([(x3, y3), (x4, y3)], fill=wall)
