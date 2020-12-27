class PocketDimension:

  def __init__(self, data: str):

    self.size = len(data[0].strip())
    self.offset = 10
    self.cubes = [[[0 for z in range(self.size + 2 * self.offset)] for y in range(self.size + 2 * self.offset)] for x in range(self.size + 2 * self.offset)]

    x_init = x = (self.size // 2 * -1) + self.offset
    y = (self.size // 2) + self.offset
    z = self.offset
    for line in data:
      for cube in line.strip():
        # add cube in initial plane
        self.cubes[x][y][z] = 1 if cube == '#' else 0
        x += 1
      x = x_init
      y -= 1

  def set_active(self, cube, active = 0):

    self.cubes[cube[0] + self.offset][cube[1] + self.offset][cube[2] + self.offset] = active

  def get_cubes(self):

    for z in range(self.size // 2 * -1, self.size // 2 + 1):
      for y in range(self.size // 2 * -1, self.size // 2 + 1):
        for x in range(self.size // 2 * -1, self.size // 2 + 1):
          yield ((x,y,z), self.cubes[x + self.offset][y + self.offset][z + self.offset])

  def get_size(self):
    return self.size

  def expand(self):

    self.size += 2

  def count_active_neighbors(self, cube):

    count = 0
    valid_range = range(self.size // 2 * -1, self.size // 2 + 1)

    for z in range(cube[2] - 1, cube[2] + 2):
      for y in range(cube[1] - 1, cube[1] + 2):
        for x in range(cube[0] - 1, cube[0] + 2):
          if x in valid_range and y in valid_range and z in valid_range \
              and (x,y,z) != cube and self.cubes[x+self.offset][y+self.offset][z+self.offset]:
            count += 1

    return count

  def count_ative_cubes(self):

    count = 0
    for z in range(self.size // 2 * -1, self.size // 2 + 1):
      for y in range(self.size // 2 * -1, self.size // 2 + 1):
        for x in range(self.size // 2 * -1, self.size // 2 + 1):
          if self.cubes[x+self.offset][y+self.offset][z+self.offset]:
            count += 1
    return count

with open('input.txt', 'r') as f:
  data = f.readlines()

pd = PocketDimension(data)

for cycle in range(0,6):

  pd.expand()

  switch_to_active = []
  switch_to_non_active = []

  for cube in pd.get_cubes():
    neighbors = pd.count_active_neighbors(cube[0])
    if cube[1] and neighbors not in range(2,4):
      switch_to_non_active.append(cube[0])
    if not cube[1] and neighbors == 3:
      switch_to_active.append(cube[0])

  # test if we have cubes in both lists
  assert_no_intersection = set(switch_to_active).intersection(set(switch_to_non_active))
  if assert_no_intersection:
    raise Exception('Check why cube is in both switch lists', assert_no_intersection)

  for cube in switch_to_active:
    pd.set_active(cube, 1)

  for cube in switch_to_non_active:
    pd.set_active(cube, 0)

print("Task 1:", pd.count_ative_cubes())
