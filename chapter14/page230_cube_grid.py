#!/usr/bin/env python3

from cell import Cell
from grid import Grid
from random import choice
from PIL import Image, ImageDraw

class CubeCell(Cell):
  def __init__(self, face, row, column):
    self.face = face
    Cell.__init__(self, row, column)

class CubeGrid(Grid):
  def __init__(self, dim):
    Grid.__init__(self, dim, dim)

  def dim(self):
    return self.rows

  def prepare_grid(self):
    faces = []

    for face in range(6):
      f = []
      faces.append(f)
      for row in range(self.dim()):
        r = []
        f.append(r)
        for column in range(self.dim()):
          r.append(CubeCell(face, row, column))

    return faces

  def each_face(self):
    for face in self.grid:
      yield face

  def each_row(self):
    for rows in self.each_face():
      for row in rows:
        yield row

  def random_cell(self):
    return choice(choice(choice(self.grid)))

  def __len__(self):
    return 6 * self.dim() * self.dim()

  def configure_cells(self):
    for cell in self.each_cell():
      face, row, col = cell.face, cell.row, cell.column

      cell.north = self[(face, row - 1, col)]
      cell.south = self[(face, row + 1, col)]
      cell.west  = self[(face, row, col - 1)]
      cell.east  = self[(face, row, col + 1)]

  def __getitem__(self, face_row_col):
    face = face_row_col[0]
    row = face_row_col[1]
    column = face_row_col[2]

    if face < 0 or face >= 6:
      return None

    face, row, column = self.wrap(face, row, column)

    return self.grid[face][row][column]

  def wrap(self, face, row, column):
    n = self.dim()-1

    if row < 0:
      if face == 0:
        return (4, column, 0)
      if face == 1:
        return (4, n, column)
      if face == 2:
        return (4, n-column, n)
      if face == 3:
        return (4, 0, n-column)
      if face == 4:
        return (3, 0, n-column)
      if face == 5:
        return (1, n, column)
    elif row >= self.dim():
      if face == 0:
        return (5, n-column, 0)
      if face == 1:
        return (5, 0, column)
      if face == 2:
        return (5, column, n)
      if face == 3:
        return (5, n, n-column)
      if face == 4:
        return (1, 0, column)
      if face == 5:
        return (3, n, n-column)
    elif column < 0:
      if face == 0:
        return (3, row, n)
      if face == 1:
        return (0, row, n)
      if face == 2:
        return (1, row, n)
      if face == 3:
        return (2, row, n)
      if face == 4:
        return (0, 0, row)
      if face == 5:
        return (0, n, n-row)
    elif column >= self.dim():
      if face == 0:
        return (1, row, 0)
      if face == 1:
        return (2, row, 0)
      if face == 2:
        return (3, row, 0)
      if face == 3:
        return (0, row, 0)
      if face == 4:
        return (2, 0, n-row)
      if face == 5:
        return (2, n, row)

    return (face, row, column)

  def to_png(self, cell_size = 10, inset = 0):
    inset = int(cell_size * inset)

    face_width = cell_size * self.dim()
    face_height = cell_size * self.dim()

    img_width = int(4 * face_width)
    img_height = int(3 * face_height)

    offsets = [(0, 1), (1, 1), (2, 1), (3, 1),  (1, 0), (1, 2)]

    background = (255, 255, 255)
    wall = (0, 0, 0)
    outline = (208, 208, 208)

    img = Image.new('RGB', size=(img_width + 1, img_height + 1), color=background)
    draw = ImageDraw.Draw(img)

    self.draw_outlines(draw, face_width, face_height, outline)

    for mode in ['backgrounds', 'walls']:
      for cell in self.each_cell():
        x = offsets[cell.face][0] * face_width + cell.column * cell_size
        y = offsets[cell.face][1] * face_width + cell.row * cell_size

        if inset > 0:
          self.to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
        else:
          self.to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

    return img

  def draw_outlines(self, draw, height, width, outline):
    # face #0
    draw.rectangle([(0, height), (width, height*2)], fill=outline)

    # faces #2 and #3
    draw.rectangle([(width*2, height), (width*4, height*2)], fill=outline)
    # line between faces #2 and #3
    draw.line([(width*3, height), (width*3, height*2)], fill=outline)

    # face #4
    draw.rectangle([(width, 0), (width*2, height)], fill=outline)

    # face #5
    draw.rectangle([(width, height*2), (width*2, height*3)], fill=outline)

  def to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y):
    x1, y1 = x, y
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    if mode == 'backgrounds':
      color = self.background_color_for(cell)
      if color:
        draw.rectangle([x, y, x2, y2], fill=color, outline=color)
    else:
      if cell.north.face != cell.face and not cell.is_linked(cell.north):
        draw.line([(x1, y1), (x2, y1)], fill=wall)

      if cell.west.face != cell.face and not cell.is_linked(cell.west):
        draw.line([(x1, y1), (x1, y2)], fill=wall)

      if not cell.is_linked(cell.east):
        draw.line([(x2, y1), (x2, y2)], fill=wall)

      if not cell.is_linked(cell.south):
        draw.line([(x1, y2), (x2, y2)], fill=wall)
