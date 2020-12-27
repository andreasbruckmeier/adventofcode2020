class Cup:

  def __init__(self, label):

    self.label = label
    self.next_cup = None

labeling = "653427918"
game_input = [int(x) for x in labeling] + list(range(int(max(labeling)) + 1, 1000001))
max_cup_label = len(game_input)

# Fill cupholder with Cup objects
cup_holder = {label: Cup(label) for label in game_input}

# Link cups and close loop
for idx in range(1, len(game_input)):
  cup_holder[game_input[idx-1]].next_cup = cup_holder[game_input[idx]]
cup_holder[game_input[-1]].next_cup = cup_holder[game_input[0]]

# Current cup is first of game input
cc = cup_holder[game_input[0]]

# Play rounds
for i in range(0,10000000):

  # Put the three successors of the current cup in a list
  pickup = [ cc.next_cup.label, cc.next_cup.next_cup.label, cc.next_cup.next_cup.next_cup.label ]

  # Exclude pickep cups from big list (connect previous cup of first pickup (== cc) with next cup of last pickup)
  cc.next_cup = cc.next_cup.next_cup.next_cup.next_cup

  # Determine the destination cup: "with a label equal to the current cup's label minus one"
  dest = cc.label - 1

  # "If at any point in this process the value goes below the lowest value on any cup's label,
  # it wraps around to the highest value on any cup's label instead.""
  #
  # We should stop and wrap when reaching the lowest available cup label (see other solution with normal lists) ,
  # but therefore we must find it in the linked list :(
  # It should be way cheaper to instead search until we reach 0.
  if dest == 0:
    dest = max_cup_label
  while dest in pickup and dest > 0:
    dest -= 1
    if dest == 0:
      dest = max_cup_label

  # Re-Insert picked cups at destination position
  cup_holder[pickup[-1]].next_cup = cup_holder[dest].next_cup
  cup_holder[dest].next_cup = cup_holder[pickup[0]]

  # Move current cup forward
  cc = cc.next_cup

# Get two cups according to the instructions
print("Solution: {}".format(cup_holder[1].next_cup.label * cup_holder[1].next_cup.next_cup.label))
