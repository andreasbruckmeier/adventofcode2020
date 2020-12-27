#/usr/bin/env python3

timestamp = 0

with open('input.txt', 'r') as f:
  line = f.readlines()[1].split(",")

busses = map(lambda x: (x[0], int(x[1])), dict(filter(lambda x: x[1] != 'x', {i: line[i] for i in range(0, len(line))}.items())).items())

# set increment to first bus departure interval
increment = next(busses)[1]

for departure_offset, departure_interval in busses:
  while True:
    timestamp += increment
    if (timestamp + departure_offset) % departure_interval == 0:
      break
  increment *= departure_interval

print(timestamp)

