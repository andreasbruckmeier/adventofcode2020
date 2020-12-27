import re

tiles = {}
flip_list = []

class Tile:

  def __init__(self, tid):

    global tiles
    global flip_list

    self.is_white = True
    self.tid = tid
    self.ne = None
    self.se = None
    self.nw = None
    self.sw = None
    self.w = None
    self.e = None

    if self.tid not in tiles:
      tiles[self.tid] = self

  def build_missing_links(self):

    # build direct connections to neighbours
    for adjacent in ['ne', 'se', 'nw', 'sw', 'w', 'e']:
      if not getattr(self, adjacent):
        getattr(self, 'add_' + adjacent)(Tile(self.tid + '-' + adjacent))

    # build connections between neigbours in circle around self
    if not self.ne.w:
      self.ne.add_w(self.nw)
    if not self.ne.se:
      self.ne.add_se(self.e)
    if not self.e.sw:
      self.e.add_sw(self.se)
    if not self.se.w:
      self.se.add_w(self.sw)
    if not self.sw.nw:
      self.sw.add_nw(self.w)
    if not self.w.ne:
      self.w.add_ne(self.nw)

  def add_ne(self, tile):

    self.ne = tile
    tile.sw = self

  def add_se(self, tile):

    self.se = tile
    tile.nw = self

  def add_nw(self, tile):

    self.nw = tile
    tile.se = self

  def add_sw(self, tile):

    self.sw = tile
    tile.ne = self

  def add_w(self, tile):

    self.w = tile
    tile.e = self

  def add_e(self, tile):

    self.e = tile
    tile.w = self

  def flip(self):

    self.is_white = not self.is_white

  def mark_for_flip(self):

    # count adjacent blacks
    count_black_adjacent = 0
    for adjacent in ['ne', 'se', 'nw', 'sw', 'w', 'e']:
      count_black_adjacent = count_black_adjacent + 1 \
        if not getattr(self, adjacent).is_white else count_black_adjacent

    # Any black tile with zero or more than 2 black tiles 
    # immediately adjacent to it is flipped to white.
    if not self.is_white and (count_black_adjacent == 0 or count_black_adjacent > 2) \
      and self.tid not in flip_list:
        flip_list.append(self.tid)

    # Any white tile with exactly 2 black tiles immediately 
    # adjacent to it is flipped to black.
    if self.is_white and (count_black_adjacent == 2) and self.tid not in flip_list:
        flip_list.append(self.tid)

def count_black_tiles():
  count = 0
  for tile in tiles:
    if not tiles[tile].is_white:
      count += 1
  return count

# Reference tile
ref = Tile('ref')

# this function walks over the grid and applies a function
# to all tiles
def on_each_tile(operation):

  # "Grid" with fixed size (might waste resource but does the job)
  for distance in range(1, 100):

    # start at ref
    tile = ref
    getattr(tile, operation)()

    # move out distance to NE
    for i in range(distance):
      tile = tile.ne
      getattr(tile, operation)()

    # move distance SE
    for i in range(distance):
      tile = tile.se
      getattr(tile, operation)()

    # move distance SW
    for i in range(distance):
      tile = tile.sw
      getattr(tile, operation)()

    # move distance W
    for i in range(distance):
      tile = tile.w
      getattr(tile, operation)()

    # move distance NW
    for i in range(distance):
      tile = tile.nw
      getattr(tile, operation)()

    # go distance steps NE
    for i in range(distance):
      tile = tile.ne
      getattr(tile, operation)()

    # move distance - 1 E
    for i in range(distance - 1):
      tile = tile.e
      getattr(tile, operation)()

# Build grid
on_each_tile('build_missing_links')

# Apply input instructions to grid and flip identified tiles
regex = re.compile('ne|se|nw|sw|w|e')
with open('input.txt', 'r') as f:
  for line in f.readlines():
    t = ref
    for direction in regex.findall(line):
      t = getattr(t, direction)
    t.flip()

# task 1
print("Task 1 (count black): {}".format(count_black_tiles()))

# task 2
for day in range(1,101):

  # add matching tiles to flip list
  on_each_tile('mark_for_flip')

  # flip marked tiles
  for tile in flip_list:
    tiles[tile].flip()

  # reset flip list
  flip_list = []

print("Task 2 (count black): {}".format(count_black_tiles()))
