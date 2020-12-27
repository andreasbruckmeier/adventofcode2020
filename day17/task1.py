class Cube:

  def __init__(self, coordinates, active = False):
    self.coordinates = coordinates
    self.active = active

  def is_active(self):
    return self.active

  def set_active(self, active = False):
    self.active = active

  def get_coordinates(self):
    return self.coordinates

class PocketDimension:

  def __init__(self, data: str):
    self.size = len(data[0].strip())
    self.cubes = {}
    x_init = x = self.size // 2 * -1
    y = x * -1
    z = 0
    for line in data:
      for cube in line.strip():
        self.cubes[(x,y,z)] = Cube((x,y,z), cube == '#')
        self.cubes[(x,y,z-1)] = Cube((x,y,z-1), False)
        self.cubes[(x,y,z+1)] = Cube((x,y,z+1), False)
        x += 1
      x = x_init
      y -= 1  

  def add_cube(self, coordinates, active = False):
    self.cubes[coordinates] = Cube(coordinates, active)

  def get_cubes(self):
    for cube in self.cubes:
      yield self.cubes[cube]

  def get_cube(self, coordinates):
    return self.cubes[coordinates]

  def get_size(self):
    return self.size

  def visualize(self):
    for z in range(self.size // 2 * -1, self.size // 2 + 1):
      print("z={}".format(z))
      for y in range(self.size // 2, self.size // 2 * -1 - 1, -1):
        for x in range(self.size // 2 * -1, self.size // 2 + 1):
          print('#' if self.cubes[(x,y,z)].active else '.', end='')
        print()
      print()

  def expand(self):
    self.size += 2
    for z in range(self.size // 2 * -1, self.size // 2 + 1):
      for y in range(self.size // 2, self.size // 2 * -1 - 1, -1):
        for x in range(self.size // 2 * -1, self.size // 2 + 1):
          if (x,y,z) not in self.cubes:
            self.cubes[(x,y,z)] = Cube((x,y,z))

  def count_active_neighbors(self, cube):
    count = 0
    cc = cube.get_coordinates()
    valid_range = range(self.size // 2 * -1, self.size // 2 + 1)
    for z in range(cc[2] - 1, cc[2] + 2):
      for y in range(cc[1] - 1, cc[1] + 2):
        for x in range(cc[0] - 1, cc[0] + 2):
          if x in valid_range and y in valid_range and z in valid_range \
              and (x,y,z) != cc and self.cubes[(x,y,z)].is_active():
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
    neighbors = pd.count_active_neighbors(cube)
    if cube.is_active() and neighbors not in range(2,4):
      switch_to_non_active.append(cube.get_coordinates())
    if not cube.is_active() and neighbors == 3:
      switch_to_active.append(cube.get_coordinates())

  for cube in switch_to_active:
    pd.get_cube(cube).set_active(True)

  for cube in switch_to_non_active:
    pd.get_cube(cube).set_active(False)

count_active = 0
for cube in pd.get_cubes():
  if cube.is_active():
    count_active += 1

print("Task 1:", count_active)
