#!/usr/bin/env python3

from page059_colored_grid import ColoredGrid
from page057_aldous_broder import AldousBroder

for n in range(6):
  grid = ColoredGrid(20, 20)
  AldousBroder.on(grid)

  middle = grid[(grid.rows//2, grid.columns//2)]
  grid.set_distances(middle.distances())

  filename = 'aldous_broder_0' + str(n) + '.png'
  grid.write_png(filename)
  print('saved to', filename)
