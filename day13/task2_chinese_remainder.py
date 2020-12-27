#/usr/bin/env python3
from functools import reduce

def extended_gcd(a, b):
    if a == 0 :   
        return b,0,1
    gcd,x1,y1 = extended_gcd(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1  
    return gcd,x,y 

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

with open('input.txt', 'r') as f:
  solution = 0
  line = f.readlines()[1].split(",")
  busses = dict(map(lambda x: (x[0], int(x[1])), dict(filter(lambda x: x[1] != 'x', {i: line[i] for i in range(0, len(line))}.items())).items()))
  bus_gcd = reduce(lambda a,b: a*b, busses.values())
  for idx, val in busses.items():
    if val == 'x':
      continue
    tmp = -idx * extended_gcd(val, bus_gcd // val)[2] * (bus_gcd // val)
    solution += tmp
  print(int(solution % bus_gcd))

