#!/usr/bin/env python3
import itertools as it

def find_set(file, target, offset, count = 0):
  for i in range(offset, len(file)):
    count += file[i]
    if count > target:
      return False
    if count == target:
      return min(file[offset:i+1]) + max(file[offset:i+1])

with open('input.txt', 'r') as f:
  file = list(map(int, f))
  preamble = 25

  # task 1
  failure = 0
  for x in range(preamble, len(file)):
    if not file[x] in [sum(i) for i in list(it.combinations(file[x-preamble:x], 2))]:
      failure = file[x]
      break

  # task 2
  range_sum = 0
  for x in range(0, len(file)):
    range_sum = find_set(file, failure, x)
    if range_sum:
      break

  print("Task 1: {}\nTask 2: {}".format(failure, range_sum))
