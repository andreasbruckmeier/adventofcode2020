#!/usr/bin/env python3

with open('input.txt', 'r') as f:
  adapters = list(map(int, f))
  output = 0
  while output <= max(adapters):
    best_adapter = min(list(filter(lambda x: x > output and x <= output + 3, adapters)))
    adapters[adapters.index(best_adapter)] = (best_adapter - output) * -1
    output = best_adapter
  print("Product: {}".format(len(list(filter(lambda x: x == -1, adapters))) * (len(list(filter(lambda x: x == -3, adapters))) + 1)))
