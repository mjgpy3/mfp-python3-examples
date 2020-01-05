#!/usr/bin/env python3

from page038_distances import Distances

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
    return cell in self.links

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

  def distances(self):
    distances = Distances(self)
    frontier = [self]

    while frontier:
      new_frontier = []

      for cell in frontier:
        for linked in cell.links:
          if distances[linked] != None:
            continue

          distances[linked] = distances[cell] + 1
          new_frontier.append(linked)

      frontier = new_frontier

    return distances
