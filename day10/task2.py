#!/usr/bin/env python3
from itertools import chain, combinations

def combine_adapters(adapters, maximum, output = 0):
  count = 1
  matching = list(filter(lambda x: x > output and x <= output + 3, adapters))
  remaining = [x for x in adapters if x not in matching]
  matching_combos = chain(*map(lambda x: combinations(matching, x), range(0, len(matching)+1)))
  if not remaining:
    return len(list(filter(lambda x: x and min(x) - output <= 3 and max(x) == maximum, matching_combos)))
  count *= len(list(filter(lambda x: x and min(x) - output <= 3 and max(x) >= remaining[0] -3, matching_combos)))
  count *= combine_adapters([x for x in adapters if x not in matching], maximum, max(matching) if len(matching) > 1 else matching[0])
  return count

with open('input.txt', 'r') as f:
  adapters = sorted(list(map(int, f)))
  print(combine_adapters(adapters, max(adapters)))