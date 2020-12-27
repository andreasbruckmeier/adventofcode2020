#!/usr/bin/env python3

def run_program(code, fix = 0):
  lines = {}
  acc = 0
  idx = 0
  while idx < len(file):
    if idx in lines:
      break
    else:
      lines[idx] = 1
    if file[idx][0:3] == 'acc':
      acc += int(file[idx][4:])
    elif (file[idx][0:3] == 'jmp' and idx != fix) or (file[idx][0:3] == 'nop' and idx == fix):
      idx += int(file[idx][4:]) - 1 if int(file[idx][4:]) != 0 else 0
    idx += 1
  return idx, acc

with open('input.txt', 'r') as f:
  file = f.read().split('\n')
  fix = 0
  while True:
    (idx, acc) = run_program(file, fix)
    if idx == len(file):
      print("ACC: " + str(acc))
      break
    fix += 1
