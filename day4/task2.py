#!/usr/bin/env python3
import re

fields = {
  "byr": (1, lambda x:(int(x) in range(1920,2003))),
  "iyr": (2, lambda x:(int(x) in range(2010,2021))),
  "eyr": (4, lambda x:(int(x) in range(2020,2031))),
  "hgt": (8, lambda x:((x[-2:] == "cm" and int(x[:-2]) in range(150,194)) or (x[-2:] == "in" and int(x[:-2]) in range(59,77)))),
  "hcl": (16, lambda x:(re.match('^#[0-9a-f]{6}$', x))),
  "ecl": (32, lambda x:(x in ["amb","blu","brn","gry","grn","hzl","oth"])),
  "pid": (64, lambda x:(re.match('^[0-9]{9}$', x))),
  "cid": (128,)
}

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

count = 0
for line in data:
  check = 0
  for field in line.split():
    fieldname = field.split(":")[0]
    if fieldname in fields:
      if fields[fieldname][0] < 128 and len(fields[fieldname]) > 1 and fields[fieldname][1](field.split(":")[1]):
        check |= fields[fieldname][0]
  if check in [127,255]:
    count += 1

print("correct: {}".format(count))

