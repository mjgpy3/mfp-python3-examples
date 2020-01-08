#!/usr/bin/env python3

from cell import Cell

class TriangleCell(Cell):
  def is_upright(self):
    return (self.row + self.column) % 2 == 0

  def neighbors(self):
    list = []

    if self.west:
      list.append(self.west)

    if self.east:
      list.append(self.east)

    if not self.is_upright() and self.north:
      list.append(self.north)

    if self.is_upright() and self.south:
      list.append(self.south)

    return list
