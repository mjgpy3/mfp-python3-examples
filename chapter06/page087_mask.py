#!/usr/bin/env python3

from random import randrange
import png

class Mask:
  @staticmethod
  def from_txt(file):
    with open(file, 'r') as f:
      lines = [line.strip() for line in f.readlines() if line]

    rows = len(lines)
    columns = len(lines[0])
    mask = Mask(rows, columns)

    for row in range(mask.rows):
      for col in range(mask.columns):
        if lines[row][col] == 'X':
          mask[(row, col)] = False
        else:
          mask[(row, col)] = True

    return mask

  @staticmethod
  def from_png(file):
    with open(file, 'rb') as f:
      image = png.Reader(file=f).read()
      pixels = [[i for i in row] for row in image[2]]
      black = (0, 0, 0)
      mask = Mask(image[3]['size'][1], image[3]['size'][0])

      for row in range(mask.rows):
        for col in range(0, len(pixels[0]), 3):
          if tuple(pixels[row][col_i] for col_i in range(col, col+3)) == black:
            mask[(row, col//3)] = False
          else:
            mask[(row, col//3)] = True

      return mask

  def __init__(self, rows, columns):
    self.rows, self.columns = rows, columns
    self.bits = [[True for _ in range(columns)] for _ in range(rows)]

  def __getitem__(self, row_col):
    row = row_col[0]
    column = row_col[1]

    if (0 <= row and row < self.rows) and (0 <= column and column < self.columns):
      return self.bits[row][column]

    return False

  def __setitem__(self, row_col, is_on):
    self.bits[row_col[0]][row_col[1]] = is_on

  def __len__(self):
    count = 0

    for row in range(self.rows):
      for col in range(self.columns):
        if self.bits[row][col]:
          count += 1

    return count

  def random_location(self):
    while True:
      row = randrange(0, self.rows)
      col = randrange(0, self.columns)

      if self.bits[row][col]:
        return (row, col)
