#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  input = list(map(str, f))
  timestamp = int(input[0].strip())
  busses = list(map(int, filter(lambda x: x != "x", input[1].strip().split(","))))
  candidate_busses = {}
  best = (timestamp, 0)
  for bus in busses:
    tours = int(timestamp / bus)
    best_match = min((filter(lambda x: x >= timestamp, map(lambda x: (x + tours) * bus, range(-1,2)))))
    if best_match - timestamp < best[0]:
      best = (best_match - timestamp, bus)
  print(best[0] * best[1])
