#!/usr/bin/env python3

lines = {}
acc = 0

with open('input.txt', 'r') as f:
  file = f.read().split('\n')
  idx = 0
  while idx < len(file):
    if idx in lines:
      print("ACC:"  + str(acc))
      break
    else:
      lines[idx] = 1
    if file[idx][0:3] == 'acc':
      acc += int(file[idx][4:])
    elif file[idx][0:3] == 'jmp':
      idx += int(file[idx][4:]) - 1
    idx += 1
