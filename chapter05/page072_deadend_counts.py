#!/usr/bin/env python3

from grid import Grid
from binary_tree import BinaryTree
from side_winder import SideWinder
from aldous_broder import AldousBroder
from page069_hunt_and_kill import HuntAndKill 
from wilsons import Wilsons

algorithms = [BinaryTree, SideWinder, AldousBroder, Wilsons, HuntAndKill]

tries = 100
size = 20

averages = {}
for algorithm in algorithms:
  print('running', algorithm.__name__)

  deadend_counts = []

  for _ in range(tries):
    grid = Grid(size, size)
    algorithm.on(grid)
    deadend_counts.append(len(grid.deadends()))

  total_deadends = sum(deadend_counts)
  averages[algorithm] = total_deadends / len(deadend_counts)

total_cells = size*size
print('')
print(f'Average dead-ends per {size}x{size} maze ({total_cells} cells):')

sorted_algorithms = sorted(algorithms, key=lambda a: -averages[a])

for algorithm in sorted_algorithms:
  percentage = averages[algorithm] * 100.0 / (size*size)
  print(f'{algorithm.__name__:14} : {round(averages[algorithm]):3}/{total_cells} ({round(percentage)}%)')
