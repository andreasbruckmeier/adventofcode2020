#!/usr/bin/env python3
import re

def find_bags(data, color, parents = []):
  contained = list(filter(lambda x: not x.startswith(color + " bag") and color in x, data))
  for bag in contained:
    m = re.match('^(.*) bags contain.*', bag)
    parent = m.group(1)
    if parent not in parents:
      parents.append(parent)
    else:
      continue
    if not find_bags(data, parent) and parent not in parents:
        parents.append(parent)
  return parents

with open('input.txt', 'r') as file:
  print(len(find_bags(file.read().split('\n'), "shiny gold")))
