#/usr/bin/env python3

initial_values = [1,20,11,6,12,0]
game_length = 30000000
brain = {}

def put_brain(number, idx):
    if not number in brain:
        brain[number] = (idx, None)
    elif not brain[number][1]:
        brain[number] = (brain[number][0], idx)
    else:
        brain[number] = (brain[number][1], idx)

# prefill brain
for idx in range(len(initial_values)):
    brain[initial_values[idx]] = (idx, None)
    last = initial_values[idx]

# play initial_values
for idx in range(len(initial_values), game_length):
    if last not in brain or not brain[last][1]:
        put_brain(0, idx)
        last = 0
    else:
        tmp = brain[last][1] - brain[last][0]
        last = tmp
        put_brain(tmp, idx)

print(last)

