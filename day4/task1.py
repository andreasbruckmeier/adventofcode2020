#!/usr/bin/env python3
import re

fields = {
  "byr": 1, "iyr": 2, "eyr": 4, "hgt": 8,
  "hcl": 16, "ecl": 32, "pid": 64, "cid": 128
}

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

count = 0
for line in data:
  check = 0
  for field in line.split():
    fieldname = field.split(":")[0]
    if fieldname in fields:
      check |= fields[fieldname]
  if check in [127,255]:
    count += 1

print("correct: {}".format(count))
