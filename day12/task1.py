#!/usr/bin/env python3

position = [0,0]
direction = 90

with open('input.txt', 'r') as f:

  for instruction in map(str, f):
  
    action = instruction[0:1]
    value = int(instruction.strip()[1:])

    if action == "F":
      if direction == 270:
        position[1] -= value
      elif direction == 90:
        position[1] += value
      elif direction == 0:
        position[0] += value
      elif direction == 180:
        position[0] -= value
    elif action == "E":
      position[1] += value
    elif action == "N":
      position[0] += value
    elif action == "W":
      position[1] -= value
    elif action == "S":
      position[0] -= value
    elif action == "R":
      direction = (direction + value) % 360
    elif action == "L":
      direction = (direction - value) % 360

  print("Position: {} {}, Manhattan distance: {}".format(position[0], 
          position[1], abs(position[0]) + abs(position[1])))
