#!/usr/bin/env python3

from random import randrange

class RecursiveDivision:
  @staticmethod
  def on(grid):
    for cell in grid.each_cell():
      for n in cell.neighbors():
        cell.link(n, False)

    RecursiveDivision.divide(grid, 0, 0, grid.rows, grid.columns)

  @staticmethod
  def divide(grid, row, column, height, width):
    if height <= 1 or width <= 1 or height < 5 and width < 5 and randrange(4) == 0:
      return

    if height > width:
      RecursiveDivision.divide_horizontally(grid, row, column, height, width)
    else:
      RecursiveDivision.divide_vertically(grid, row, column, height, width)

  @staticmethod
  def divide_horizontally(grid, row, column, height, width):
    divide_south_of = randrange(height-1)
    passage_at = randrange(width)

    for x in range(width):
      if passage_at == x:
        continue

      cell = grid[(row+divide_south_of, column+x)]
      cell.unlink(cell.south)

    RecursiveDivision.divide(grid, row, column, divide_south_of+1, width)
    RecursiveDivision.divide(grid, row+divide_south_of+1, column, height-divide_south_of-1, width)

  @staticmethod
  def divide_vertically(grid, row, column, height, width):
    divide_east_of = randrange(width-1)
    passage_at = randrange(height)

    for y in range(height):
      if passage_at == y:
        continue

      cell = grid[(row+y, column+divide_east_of)]
      cell.unlink(cell.east)

    RecursiveDivision.divide(grid, row, column, height, divide_east_of+1)
    RecursiveDivision.divide(grid, row, column+divide_east_of+1, height, width-divide_east_of-1)
