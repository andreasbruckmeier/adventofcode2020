from collections import deque

class Game():

  def __init__(self, labeling):

    self.cups = deque([int(x) for x in labeling])
    self.current_cup = self.cups[0]
    self.pickup = None

  def draw(self):
    print("cups: ", end='')
    for idx in range(len(self.cups)):
      if self.cups[idx] == self.current_cup:
        print("(" + str(self.cups[idx]) + ") ", end='')
      else:
        print(str(self.cups[idx]) + " ", end='')
    print()

  def move_cc(self):
    tmp_cc = self.cups.index(self.current_cup) + 1
    if tmp_cc >= len(self.cups):
      tmp_cc = 0
    self.current_cup = self.cups[tmp_cc]
    return self.current_cup

  def do_pickup(self, num = 3):

    ccidx = self.cups.index(self.current_cup)
    self.cups.rotate(-ccidx -1)
    self.pickup = [self.cups.popleft(), self.cups.popleft(), self.cups.popleft()]
    return self.pickup

  def do_insert(self, dst):

    insert_idx = self.cups.index(dst)
    #print("INSERT", self.cups, self.pickup)
    self.pickup.reverse()
    self.cups.rotate(-insert_idx-1)
    self.cups.extendleft(self.pickup)
    #for pick in self.pickup:
    #  self.cups.rotate(-1)
    #  self.cups.insert(0, pick)

  def choose_desination(self):

    dst = self.current_cup - 1
    if dst < min(self.cups):
      return max(self.cups)
    while dst in self.pickup and dst >= min(self.cups):
      dst -= 1
    if dst < min(self.cups):
      dst = self.cups[-1]
    return dst

g = Game("653427918")

for i in range(0,100):

  g.do_pickup()
  g.do_insert(g.choose_desination())
  g.move_cc()

# solution
g.cups.rotate(-g.cups.index(1)-1)
g.cups.pop()
print(''.join(map(str, g.cups)))
