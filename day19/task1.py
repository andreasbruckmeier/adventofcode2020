#/usr/bin/env python3
import re

rules = True
messages = []
ruleset = {}

def process_rules(rule):
  while True:
    new_rule = []
    count_replacements = 0
    for idx in range(0, len(rule)):
      if rule[idx] in "ab()|":
        new_rule += rule[idx]
      else:
        if "|" in ruleset[rule[idx]]:
          new_rule += ["("] + ruleset[rule[idx]] + [")"]
          count_replacements += 1
        else:
          new_rule += ruleset[rule[idx]]
          count_replacements += 1
    if not count_replacements:
      return ''.join(new_rule)
    rule = new_rule

with open('input.txt', 'r') as f:
  for line in list(map(str.strip, (map(str, f)))):
    if not line:
      rules = False
      continue
    if rules:
      rule_number, rule = line.split(":")
      ruleset[rule_number] = rule.strip().replace('"', '').split(" ")
    else:
      messages.append(line)

prog = re.compile('^' + process_rules(ruleset['0'].copy()) + '$')

count = 0
for m in messages:
  if prog.match(m):
    count += 1

print(count)
