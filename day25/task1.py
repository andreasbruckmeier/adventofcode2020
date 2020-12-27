def get_loop_size(pubkey, subject = 7, value = 1, fixed = 20201227):

  loopsize = 0
  while value != pubkey:
    value *= subject
    value %= fixed
    loopsize += 1
  return loopsize

def get_encryption_key(pubkey, loopsize, value = 1, fixed = 20201227):

  for i in range(loopsize):
    value *= pubkey
    value %= fixed
  return value

with open('input.txt', 'r') as f:
  pubkeys = list(map(int, f))
  loopsizes = [get_loop_size(pubkeys[0]), get_loop_size(pubkeys[1])]
  print(get_encryption_key(pubkeys[0], loopsizes[1]))
