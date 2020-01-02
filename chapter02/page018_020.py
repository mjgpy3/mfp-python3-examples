#!/usr/bin/env python3

class Cell:
  def __init__(self, row, column):
    self.row = row
    self.column = column
    self.links = {}
    self.north = None
    self.south = None
    self.east = None
    self.west = None

  def link(self, cell, bidi=True):
    self.links[cell] = True
    if bidi:
      cell.link(self, False)

    return self

  def unlink(self, cell, bidi=True):
    del self.links[cell]
    if bidi:
      cell.unlink(self, False)

    return self

  def get_links(self):
    return list(self.links.keys())

  def is_linked(self, cell):
    return cell in links

  def neighbors(self):
    list = []

    if self.north:
      list.append(self.north)

    if self.south:
      list.append(self.south)

    if self.east:
      list.append(self.east)

    if self.west:
      list.append(self.west)

    return list
