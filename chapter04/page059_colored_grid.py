#!/usr/bin/env python3

from page057_grid import Grid

class ColoredGrid(Grid):

  # Cannot do specific property setters in Python
  def set_distances(self, distances):
    self.distances = distances
    farthest, self.maximum = distances.max()

  def background_color_for(self, cell):
    distance = self.distances[cell]

    if not distance:
      return (255, 255, 255)

    intensity = float(self.maximum - distance) / self.maximum
    dark = round(255 * intensity)
    bright = 128 + round(127 * intensity)
    return (dark, bright, dark)
