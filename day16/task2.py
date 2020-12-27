#/usr/bin/env python3
import re

rules = {}
rules_input = []
my_ticket = []
nearby_tickets = []
rule_regex = re.compile('^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$')

valid_tickets = []
field_map = {}

with open('input.txt', 'r') as f:
  container = rules_input
  for line in list(map(str, f)):
    stripped = line.strip()
    if not stripped:
      continue
    if line[0:4] == 'your':
      container = my_ticket
      continue
    if line[0:4] == 'near':
      container = nearby_tickets
      continue
    container.append(stripped)

my_ticket = list(map(int, my_ticket[0].split(",")))

for i in range(0,len(rules_input)):
  rule = rule_regex.match(rules_input[i].strip())
  rules[rule.group(1)] = (int(rule.group(2)), int(rule.group(3)), int(rule.group(4)), int(rule.group(5)), -1)

def check_ticket(ticket):
  sum_wrong = 0
  for field in ticket:
    v = int(field)
    if len(list(filter(lambda x: (v >= x[0] and v <= x[1]) or (v >= x[2] and v <= x[3]), rules.values()))) == 0:
      sum_wrong += int(field)
  return sum_wrong

for nearby_ticket in nearby_tickets:
  nearby_ticket = nearby_ticket.split(",")
  if not check_ticket(nearby_ticket):
    valid_tickets.append(nearby_ticket)

field_names = {}
field_rule_candidates = {}

for i in range(0, len(valid_tickets[0])):
  matching_rules = []
  for valid_ticket in valid_tickets:
    field_value = int(valid_ticket[i])
    matching_rules += [name for name, cond in rules.items() if (field_value >= cond[0] and field_value <= cond[1]) or (field_value >= cond[2] and field_value <= cond[3])]
  matching_rules_distribution = {i:matching_rules.count(i) for i in matching_rules}
  field_rule_candidates[i] = [k for k, v in matching_rules_distribution.items() if v == max(matching_rules_distribution.values())]

field_mapping = {}

for k, v in sorted(field_rule_candidates.items(), key=lambda item: len(item[1])):
  if len(v) == 1:
    field_mapping[v[0]] = k
  else:
    for f in v:
      if f not in field_mapping:
        field_mapping[f] = k

result = 1

for f in field_mapping:
  if f[0:2] == "de":
    result *= my_ticket[field_mapping[f]]

print(result)
