#!/usr/bin/env python3

from random import choice

class SideWinder:
  @staticmethod
  def on(grid):
    for row in grid.each_row():
      run = []

      for cell in row:
        run.append(cell)

        at_eastern_boundary = not cell.east
        at_northern_boundary = not cell.north

        should_close_out = at_eastern_boundary or (not at_northern_boundary and choice([True, False]))

        if should_close_out:
          member = choice(run)
          if member.north:
            member.link(member.north)
          del run[:]
        else:
          cell.link(cell.east)

    return grid
