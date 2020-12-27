#!/usr/bin/env python3

with open('input.txt', 'r') as f:
  seats = []
  max_seat_id = 0
  for boarding_pass in map(str, f):
    row = int(boarding_pass[0:7].replace('F','0').replace('B', '1'),2)
    seat = int(boarding_pass[7:].replace('L','0').replace('R', '1'),2)
    seats.append(row * 8 + seat)
  occupied = list(filter(lambda x: (x-1) in seats and (x+1) in seats, seats))
  my_seat = sorted(list(filter(lambda x: x not in occupied, seats)))[1:-1][0] + 1
  print("max id: {} ".format(max(seats)))
  print("my: {} ".format(my_seat))

