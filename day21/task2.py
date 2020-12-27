#!/usr/bin/env python3
from functools import reduce

foods = []
allergens = {}

with open('input.txt', 'r') as f:
  for line in map(str.strip, (map(str, f))):
    i, a = line.split(" (contains ")
    foods.append((i.strip().split(" "), a[0:-1].split(", ")))

for food in foods:
    for allergen in food[1]:
        tmp_ing = set(food[0])
        if allergen in allergens:
            continue
        for ggg in list(map(lambda x: x[0], (filter(lambda x: allergen in x[1], foods)))):
            tmp_ing = tmp_ing.intersection(set(ggg))
        allergens[allergen] = tmp_ing

mapping = {}

search = sorted(allergens.items(), key=lambda item: len(item[1]))

for i in range(0,len(search)):
    for k, v in search:
        lv = list(v)
        if len(lv) == 1:
            mapping[lv[0]] = k
            for idx in range(0, len(search)):
                if lv[0] in search[idx][1]:
                    search[idx][1].remove(lv[0])
    

for k, v in sorted(mapping.items(), key=lambda item: item[1]):
    print(k, end=',')
