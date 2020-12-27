#!/usr/bin/env python3
import math

waypoint = [1,10]
position = [0,0]

def rotate_waypoint(position, waypoint, rotation):

  radian = math.radians(rotation)
  cos = math.cos(radian)
  sin = math.sin(radian)
  ns = position[0] + cos * (waypoint[0] - position[0]) - sin * (waypoint[1] - position[1])
  ew = position[1] + sin * (waypoint[0] - position[0]) + cos * (waypoint[1] - position[1])
  waypoint[0] = round(ns)
  waypoint[1] = round(ew)

def move_ship_and_waypoint(position, waypoint, unit):

  vdistance = (waypoint[0] - position[0]) * unit
  hdistance = (waypoint[1] - position[1]) * unit
  position[0] += vdistance
  position[1] += hdistance
  waypoint[0] += vdistance
  waypoint[1] += hdistance

with open('input.txt', 'r') as f:

  for instruction in map(str, f):

    action = instruction[0:1]
    value = int(instruction.strip()[1:])

    if action == "F":
      move_ship_and_waypoint(position, waypoint, value)
    elif action == "E":
      waypoint[1] += value
    elif action == "N":
      waypoint[0] += value
    elif action == "W":
      waypoint[1] -= value
    elif action == "S":
      waypoint[0] -= value
    elif action == "R":
      rotate_waypoint(position, waypoint, value)
    elif action == "L":
      rotate_waypoint(position, waypoint, -value)

  print("Position: {} {}, Manhattan distance: {}".format(position[0], 
          position[1], abs(position[0]) + abs(position[1])))

