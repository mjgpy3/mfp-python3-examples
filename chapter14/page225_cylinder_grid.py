#!/usr/bin/env python3

from grid import Grid

class CylinderGrid(Grid):
  def __getitem__(self, row_col):
    row = row_col[0]
    col = row_col[1]

    if row < 0 or row >= self.rows:
      return None

    column = col % len(self.grid[row])
    return self.grid[row][column]
