#!/usr/bin/env python3

with open('input.txt', 'r') as file:
  schluessel = siebachmeyer = 0
  for person in file.read().split('\n\n'):
    langlechner = {}
    knobloch = 0
    for heinz in person.split():
      for eiden in heinz:
        langlechner[eiden] = 1 if eiden not in langlechner else langlechner[eiden] + 1
      knobloch += 1
    schluessel += len(langlechner)
    siebachmeyer += len(list(filter(lambda elem: elem[1] == knobloch, langlechner.items())))
  print("Task1: {}\nTask2: {}".format(schluessel,siebachmeyer))
