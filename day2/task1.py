with open('input.txt') as f:
  correct = 0
  for password in map(str, f):
    (policy, character, password) = password.split()
    (policy_min, policy_max) = policy.split('-')
    character = character[:-1]
    if password.count(character) in range(int(policy_min), int(policy_max)+1):
      correct += 1
  print(correct)
