#/usr/bin/env python3
import re

rules = True
messages = []
ruleset = {}
transformed_rules = []

revisits = {"8": 0, "11": 0}

def process_rules(rule):

  while True:
    new_rule = []
    count_replacements = 0
    for idx in range(0, len(rule)):
      if rule[idx] in "ab()|":
        new_rule += rule[idx]
      else:
        # replace looping element by any valid non looping rule
        # after some revisits in order to break the loop but still
        # get a long enough regex to match the longest string
        if rule[idx] in ["8","11"]:
          if revisits[rule[idx]] > 100:
            rule[idx] = "12"
          else:
            revisits[rule[idx]] += 1
        if "|" in ruleset[rule[idx]]:
          new_rule += ["("] + ruleset[rule[idx]] + [")"]
          count_replacements += 1
        else:
          new_rule += ruleset[rule[idx]]
          count_replacements += 1

    if not count_replacements:
      return ''.join(new_rule)

    rule = new_rule

with open('input_task2.txt', 'r') as f:
  for line in list(map(str.strip, (map(str, f)))):
    if not line:
      rules = False
      continue
    if rules:
      rule_number, rule = line.split(":")
      ruleset[rule_number] = rule.strip().replace('"', '').split(" ")
    else:
      messages.append(line)


regex_rule = process_rules(ruleset['0'].copy())

prog = re.compile('^' + regex_rule + '$')

count = 0
for m in messages:
  if prog.match(m):
    count += 1

print(count)
