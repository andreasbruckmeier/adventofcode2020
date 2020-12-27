#!/usr/bin/env python3

def find(numbers, sum): 
  for i in range(len(numbers) - 1): 
    for j in range(i + 1, len(numbers)):
      if numbers[j] + numbers[i] == 2020: 
        print("Found: {} * {} = {}".format(numbers[i], numbers[j], numbers[j] * numbers[i])) 
        return

with open('input.txt') as f:
  find(list(map(int, f)), 2020)

