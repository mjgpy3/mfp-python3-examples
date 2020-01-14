#!/usr/bin/env python3

from grid import Grid
from page134_weighted_cell import WeightedCell

class WeightedGrid(Grid):
  def __init__(self, rows, columns):
    Grid.__init__(self, rows, columns)
    self.distances = None

  # No overloaded prop setters in Python
  def set_distances(self, distances):
    self.distances = distances
    self.farthest, self.maximum = distances.max()

  def prepare_grid(self):
    return [[WeightedCell(row, column) for column in range(self.columns)] for row in range(self.rows)]

  def background_color_for(self, cell):
    if cell.weight > 1:
      return (255, 0, 0)
    elif self.distances:
      distance = self.distances[cell]

      if not distance:
        return super()

      intensity = 64 + 191 * (self.maximum - distance) / self.maximum
      return (intensity, intensity, 0)

    return super()
