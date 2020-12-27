#!/usr/bin/env python3

def has_adjacent_occupied(area, x , y):
  area_length = len(area)
  area_width = len(area[0])
  count = 0
  for sx in range(x - 1, x + 1 + 1):
    for sy in range(y - 1, y + 1 + 1):
      if (sx == x and sy == y) or sx < 0 or sy < 0 or sx >= area_length or sy >= area_width:
        continue
      if area[sx][sy] == '#':
        count += 1
  return count

def run_sim(area):
  area_length = len(area)
  area_width = len(area[0])
  new_area = [['.' for i in range(area_width)] for j in range(area_length)]
  changes = 0
  occupied = 0
  for x in range(0, area_length):
    for y in range(0, area_width):
      if area[x][y] == 'L':
        if not has_adjacent_occupied(area, x , y):
          new_area[x][y] = '#'
          occupied += 1
          changes += 1
        else:
          new_area[x][y] = 'L'
      if area[x][y] == '#':
        if has_adjacent_occupied(area, x , y) >= 4:
          new_area[x][y] = 'L'
          changes += 1
        else:
          occupied += 1
          new_area[x][y] = '#'
  return new_area, changes, occupied

with open('input.txt', 'r') as f:
  area = []
  for line in map(str, f):
    area.append([char for char in line.strip()])

  while True:
    area, changes, occupied = run_sim(area)
    if changes == 0:
      print(occupied)
      break
