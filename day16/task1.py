#/usr/bin/env python3
import re

rules = []
my_ticket = []
nearby_tickets = []
rule_regex = re.compile('^[a-z ]+: ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$')

with open('input.txt', 'r') as f:
  container = rules
  for line in list(map(str, f)):
    if not line.strip():
      continue
    if line[0:4] == 'your':
      container = my_ticket
      continue
    if line[0:4] == 'near':
      container = nearby_tickets
      continue
    container.append(line.strip())

for i in range(0,len(rules)):
  rule = rule_regex.match(rules[i].strip())
  rules[i] = (int(rule.group(1)), int(rule.group(2)), int(rule.group(3)), int(rule.group(4)))

def check_field(value):
  valid = False
  for rule in rules:
    if value >= rule[0] and value <= rule[1]:
      valid = True
    if value >= rule[2] and value <= rule[3]:
      valid = True
  return valid

def check_ticket(ticket):

  sum_wrong = 0

  for field in ticket:
    if not check_field(int(field)):
      sum_wrong += int(field)

  return sum_wrong

sum_wrong = 0
for nearby_ticket in nearby_tickets:
  nearby_ticket = nearby_ticket.split(",")
  sum_wrong += check_ticket(nearby_ticket)

print(sum_wrong)
