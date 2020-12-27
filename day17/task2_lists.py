class PocketDimension:

  def __init__(self, data: str):

    self.size = len(data[0].strip())
    self.size_half = self.size // 2
    self.offset = 10
    self.cubes = [[[[0 for w in range(self.size + 2 * self.offset)] for z in range(self.size + 2 * self.offset)] for y in range(self.size + 2 * self.offset)] for x in range(self.size + 2 * self.offset)]

    x_init = x = (self.size // 2 * -1) + self.offset
    y = (self.size // 2) + self.offset
    z = w = self.offset
    for line in data:
      for cube in line.strip():
        self.cubes[x][y][z][w] = 1 if cube == '#' else 0
        x += 1
      x = x_init
      y -= 1

  def set_active(self, cube, active = 0):

    self.cubes[cube[0] + self.offset][cube[1] + self.offset][cube[2] + self.offset][cube[3] + self.offset] = active

  def get_cubes(self):

    min = self.size_half * -1
    max = self.size_half + 1

    for w in range(min, max):
      for z in range(min, max):
        for y in range(min, max):
          for x in range(min, max):
            yield ((x,y,z,w), self.cubes[x + self.offset][y + self.offset][z + self.offset][w + self.offset])

  def expand(self):

    self.size += 2
    self.size_half = self.size // 2

  def count_active_neighbors(self, cube):

    count = 0
    valid_range = range(self.size_half * -1, self.size_half + 1)

    min_w = cube[3] - 1
    max_w = cube[3] + 2
    min_z = cube[2] - 1
    max_z = cube[2] + 2
    min_y = cube[1] - 1
    max_y = cube[1] + 2
    min_x = cube[0] - 1
    max_x = cube[0] + 2

    for w in range(min_w, max_w):
      for z in range(min_z, max_z):
        for y in range(min_y, max_y):
          for x in range(min_x, max_x):
            if x in valid_range and y in valid_range and z in valid_range \
                and (x,y,z,w) != cube and self.cubes[x+self.offset][y+self.offset][z+self.offset][w+self.offset]:
              count += 1

    return count

  def count_ative_cubes(self):

    min = self.size_half * -1
    max = self.size_half + 1
    count = 0

    for w in range(min, max):
      for z in range(min, max):
        for y in range(min, max):
          for x in range(min, max):
            if self.cubes[x+self.offset][y+self.offset][z+self.offset][w+self.offset]:
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

  for cube in switch_to_active:
    pd.set_active(cube, 1)

  for cube in switch_to_non_active:
    pd.set_active(cube, 0)

print("Task 2:", pd.count_ative_cubes())
