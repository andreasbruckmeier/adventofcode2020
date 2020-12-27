#!/usr/bin/env python3
from functools import reduce

foods = []

allergens = {}

with open('input.txt', 'r') as f:
  for line in map(str.strip, (map(str, f))):
    i, a = line.split(" (contains ")
    foods.append((i.strip().split(" "), a[0:-1].split(", ")))

# try to find ingredients which might have allergens
for food in foods:
    for allergen in food[1]:
        tmp_ing = set(food[0])
        if allergen in allergens:
            continue
        for ggg in list(map(lambda x: x[0], (filter(lambda x: allergen in x[1], foods)))):
            tmp_ing = tmp_ing.intersection(set(ggg))
        allergens[allergen] = tmp_ing

flat_list = set([item for sublist in list(map(lambda x: list(x[1]), allergens.items())) for item in sublist])
flat_list2 = set([item for sublist in list(map(lambda x: x[0], foods)) for item in sublist])

counter = 0
for searcher in flat_list2.difference(flat_list):
    counter += sum(list(map(lambda x: x[0].count(searcher), filter(lambda x: searcher in x[0], foods))))

print(counter)
