#!/usr/bin/env python3
import re

def count_bags(data, color):
  count = 1
  for bag in re.match('.*contain (.*)\\.$', next(filter(lambda x: x.startswith(color + " bag"), data))).group(1).split(", "):
    if (b := re.match('^([0-9]+) ([a-z ]+) bags?$', bag)):
      count += int(b.group(1)) * count_bags(data, b.group(2))
  return count

with open('input.txt', 'r') as file:
  print(count_bags(file.read().split('\n'), "shiny gold") - 1)
