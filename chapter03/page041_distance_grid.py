#!/usr/bin/env python3

from page040_grid import Grid

base_36s = {}

for i in range(10):
  base_36s[i] = str(i)

for (i, c) in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  base_36s[i+10] = c

class DistanceGrid(Grid):
  def __init__(self, rows, columns):
    Grid.__init__(self, rows, columns)
    self.distances = None

  def contents_of(self, cell):
    if self.distances and self.distances[cell] in base_36s:
      return base_36s[self.distances[cell]]
    if self.distances and self.distances[cell]:
      return '>'

    return super().contents_of(cell)
