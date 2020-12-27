#!/usr/bin/env python3
import re

def expand_address(address, addresses, idx = None):
  if not idx:
    address = address.lstrip('0')
    idx = len(address) - 1
  for i in range(idx, -1, -1):
    if address[i] == 'X':
      for j in ['1','0']:
        expand_address(address[0:i] + j + address[i+1:], addresses, i -1)
      break
  else:
    addresses.append(int(address, 2))
  return addresses

def mask_value(value, mask, task = 1):
  bin_value = "{0:036b}".format(value)
  masked_value = ''
  for char in range(len(bin_value) - 1, -1, -1):
    if task == 1:
      masked_value += bin_value[char] if mask[char] == 'X' else mask[char]
    else:
      masked_value += (mask[char] if mask[char] == 'X' else bin_value[char] if mask[char] == '0' else '1')
  return int(masked_value[::-1], 2) if task == 1 else masked_value[::-1]

with open('input.txt', 'r') as f:
  line_regex = re.compile('^mem\\[([0-9]*)\\] = ([0-9]*)')
  memory1 = {}
  memory2 = {}
  mask = 0
  for line in list(map(str, f)):
    if line[0:4] == 'mask':
      mask = line[7:].strip()
    else:
      m = line_regex.match(line)
      address = int(m.group(1))
      value = int(m.group(2))

      # task 1
      memory1[address] = mask_value(value, mask)

      # task 2
      addresses = []
      for add in expand_address(mask_value(address, mask, 2), addresses):
        memory2[add] = value

  print("Task 1: {}\nTask 2: {}".format(sum(memory1.values()), sum(memory2.values())))
