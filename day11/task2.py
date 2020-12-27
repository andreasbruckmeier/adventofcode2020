#!/usr/bin/env python3

def has_adjacent_occupied(area, x , y):

  area_length = len(area)
  area_width = len(area[0])
  directions = [0,0,0,0,0,0,0,0]
  distance = 1
  max_distance = max(area_length, area_width)

  while distance < max_distance:

    # left
    if directions[0] == 0 and y - distance >= 0:
      if area[x][y - distance] == '#':
        directions[0] = 1
      elif area[x][y - distance] == 'L':
        directions[0] = 2
      
    # right
    if directions[1] == 0 and y + distance < area_width:
      if area[x][y + distance] == '#':
        directions[1] = 1
      elif area[x][y + distance] == 'L':
        directions[1] = 2
      
    # top
    if directions[2] == 0 and x - distance >= 0:
      if area[x - distance][y] == '#':
        directions[2] = 1
      elif area[x - distance][y] == 'L':
        directions[2] = 2
      
    # bottom
    if directions[3] == 0 and x + distance < area_length:
      if area[x + distance][y] == '#':
        directions[3] = 1
      elif area[x + distance][y] == 'L':
        directions[3] = 2      
    
    # top left
    if directions[4] == 0 and x - distance >= 0 and y - distance >= 0:
      if area[x - distance][y - distance] == '#':
        directions[4] = 1
      elif area[x - distance][y - distance] == 'L':
        directions[4] = 2

    # top right
    if directions[5] == 0 and x - distance >= 0 and y + distance < area_width:
      if area[x - distance][y + distance] == '#':
        directions[5] = 1
      elif area[x - distance][y + distance] == 'L':
        directions[5] = 2

    # bottom left
    if directions[6] == 0 and x + distance < area_length and y - distance >= 0:
      if area[x + distance][y - distance] == '#':
        directions[6] = 1
      elif area[x + distance][y - distance] == 'L':
        directions[6] = 2

    # bottom right
    if directions[7] == 0 and x + distance < area_length and y + distance < area_width:
      if area[x + distance][y + distance] == '#':
        directions[7] = 1
      elif area[x + distance][y + distance] == 'L':
        directions[7] = 2

    distance += 1

  return len(list(filter(lambda x: x == 1, directions)))

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
        if has_adjacent_occupied(area, x , y) >= 5:
          new_area[x][y] = 'L'
          changes += 1
        else:
          occupied += 1
          new_area[x][y] = '#'
  return new_area, changes, occupied

def print_area(area):
  for line in area:
    print(''.join(line))
  print("")

with open('input.txt', 'r') as f:
  area = []
  for line in map(str, f):
    area.append([char for char in line.strip()])

  while True:
    area, changes, occupied = run_sim(area)
    #print_area(area)
    if changes == 0:
      print(occupied)
      break
