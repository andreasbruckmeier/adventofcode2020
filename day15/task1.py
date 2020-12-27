#/usr/bin/env python3

starting_numbers = [1,20,11,6,12,0]
game = starting_numbers + [None] * (2020 - len(starting_numbers))

for idx in range(0,len(game)):
    if game[idx] == None:
        try:
            t = next(i for i in range(idx-1, -1, -1) if game[i] == game[idx-1])
            try:
                t2 = next(i for i in range(t-1, -1, -1) if game[i] == game[idx-1])
                game[idx] = t - t2
            except:
                game[idx] = 0
        except:
            game[idx] = 0

print(game[-1])
