#!/usr/bin/env python3

from cell import Cell

class OverCell(Cell):
  def __init__(self, row, column, grid):
    Cell.__init__(self, row, column)
    self.grid = grid

  def neighbors(self):
    list = super().neighbors()

    if self.can_tunnel_north():
      list.append(self.north.north)

    if self.can_tunnel_south():
      list.append(self.south.south)

    if self.can_tunnel_east():
      list.append(self.east.east)

    if self.can_tunnel_west():
      list.append(self.west.west)

    return list

  def can_tunnel_north(self):
    return self.north and self.north.north and self.north.horizontal_passage()

  def can_tunnel_south(self):
    return self.south and self.south.south and self.south.horizontal_passage()

  def can_tunnel_east(self):
    return self.east and self.east.east and self.east.vertical_passage()

  def can_tunnel_west(self):
    return self.west and self.west.west and self.west.vertical_passage()

  def horizontal_passage(self):
    return (self.is_linked(self.east) and self.is_linked(self.west) and
        not self.is_linked(self.north) and not self.is_linked(self.south))

  def vertical_passage(self):
    return (self.is_linked(self.north) and self.is_linked(self.south) and
        not self.is_linked(self.east) and not self.is_linked(self.west))

  def link(self, cell, bidi=True):
    neighbor = None

    if self.north and self.north == cell.south:
      neighbor = self.north
    elif self.south and self.south == cell.north:
      neighbor = self.south
    elif self.east and self.east == cell.west:
      neighbor = self.east
    elif self.west and self.west == cell.east:
      neighbor = self.west

    if neighbor:
      self.grid.tunnel_under(neighbor)
    else:
      super().link(cell, bidi)

class UnderCell(Cell):
  def __init__(self, over_cell):
    Cell.__init__(self, over_cell.row, over_cell.column)

    if over_cell.horizontal_passage():
      self.north = over_cell.north
      over_cell.north.south = self
      self.south = over_cell.south
      over_cell.south.north = self

      self.link(self.north)
      self.link(self.south)
    else:
      self.east = over_cell.east
      over_cell.east.west = self
      self.west = over_cell.west
      over_cell.west.east = self

      self.link(self.east)
      self.link(self.west)

  def horizontal_passage(self):
    return self.east or self.west

  def vertical_passage(self):
    return self.north or self.south
