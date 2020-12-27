import re

class Tile:

  def __init__(self, number, data):
    self.data_length = len(data)
    self.width = int(self.data_length ** 0.5)
    self.number = number
    self.data = data

  def get_orientation(self, orientation):
    if orientation == 0:
      return Tile(self.number, self.data)
    elif orientation == 1:
      return self.rotate_right()
    elif orientation == 2:
      return self.rotate_right().rotate_right()
    elif orientation == 3:
      return self.rotate_right().rotate_right().rotate_right()
    elif orientation == 4:
      return self.flip_horizontal()
    elif orientation == 5:
      return self.rotate_right().flip_horizontal()
    elif orientation == 6:
      return self.rotate_right().rotate_right().flip_horizontal()
    elif orientation == 7:
      return self.rotate_right().rotate_right().rotate_right().flip_horizontal()
    else:
      raise Exception("Ivalid orientation", orientation)

  def get_all_orientations(self):
    for i in range(8):
      yield (i, self.get_orientation(i))

  def is_right_adjacent(self, tile):
    return self.get_right_edge() == tile.get_left_edge()

  def is_bottom_adjacent(self, tile):
    return self.get_bottom_edge() == tile.get_top_edge()

  def get_edges(self):
    return (self.get_left_edge(), self.get_top_edge(),
      self.get_right_edge(), self.get_bottom_edge())

  def get_left_edge(self):
    return ''.join([self.data[x * self.width] for x in range(0, self.width)])

  def get_top_edge(self):
    return ''.join([self.data[x] for x in range(0, self.width)])

  def get_right_edge(self):
    return ''.join([self.data[(x * self.width) + self.width - 1] for x in range(0, self.width)])

  def get_bottom_edge(self):
    return ''.join([self.data[(self.width - 1) * self.width + x] for x in range(0, self.width)])

  def rotate_right(self):
    new_data = ''
    for i in range(0, self.width):
      for j in range(self.width - 1, -1, -1):
        new_data += self.data[j*self.width + i]
    return Tile(self.number, new_data)

  def flip_horizontal(self):
    new_data = ''
    for i in range(0, self.width):
      for j in range(self.width - 1, -1, -1):
        new_data += self.data[i*self.width+j]
    return Tile(self.number, new_data)

tiles = {}
with open('input.txt', 'r') as f:
  for tile in f.read().strip().replace("\n", "")[5:].split("Tile "):
    number, tile = tile.split(":")
    tiles[int(number)] = Tile(int(number), tile)

edgemap = {}
# Build map of matching edges
for number, tile in tiles.items():
  for edge in tile.get_edges():
    if edge not in edgemap and edge[::-1] not in edgemap:
      edgemap[edge] = [number]
    elif edge in edgemap:
      edgemap[edge].append(number)
    else:
      edgemap[edge[::-1]].append(number)

# extract corners
corner_tiles = {}
for i,j in {k: v for k, v in edgemap.items() if len(v) == 1}.items():
  j = j[0]
  if j in corner_tiles:
    corner_tiles[j] += 1
  else:
    corner_tiles[j] = 1
corner_tiles = list({k: v for k, v in corner_tiles.items() if v > 1}.keys())

result = 1
for x in corner_tiles:
  result = result * x 
print("Task 1:", result)

image_width = int(len(tiles) ** 0.5)
num_tiles = len(tiles)

def assemble(current_tile, current_tile_orientation, processed_tiles = [], processed_tiles_orientations = []):
  num_processed_tiles = len(processed_tiles)
  if num_processed_tiles == num_tiles - 1:
    return (processed_tiles + [current_tile], processed_tiles_orientations + [current_tile_orientation])
  res = False
  if num_processed_tiles < image_width - 1:
    for tile in tiles:
      if tile == current_tile or tile in processed_tiles:
        continue
      for orientation in tiles[tile].get_all_orientations():
        if tiles[current_tile].get_orientation(current_tile_orientation).is_right_adjacent(orientation[1]):
          res = assemble(orientation[1].number, orientation[0], processed_tiles + [current_tile], processed_tiles_orientations + [current_tile_orientation])
  else:
    if num_processed_tiles % image_width < image_width - 1:
      tile_to_match = num_processed_tiles + 1 - image_width
      for tile in tiles:
        if tile == current_tile or tile in processed_tiles:
          continue
        for orientation in tiles[tile].get_all_orientations():
          if tiles[processed_tiles[tile_to_match]].get_orientation(processed_tiles_orientations[tile_to_match]).is_bottom_adjacent(orientation[1]) \
           and tiles[current_tile].get_orientation(current_tile_orientation).is_right_adjacent(orientation[1]):
            res = assemble(orientation[1].number, orientation[0], processed_tiles + [current_tile], processed_tiles_orientations + [current_tile_orientation])
    else:
      tile_to_match = num_processed_tiles - (image_width - 1)
      for tile in tiles:
        if tile == current_tile or tile in processed_tiles:
          continue
        for orientation in tiles[tile].get_all_orientations():
          if tiles[processed_tiles[tile_to_match]].get_orientation(processed_tiles_orientations[tile_to_match]).is_bottom_adjacent(orientation[1]):
            res = assemble(orientation[1].number, orientation[0], processed_tiles + [current_tile], processed_tiles_orientations + [current_tile_orientation])
  return res

def find_image():
  for corner_tile in corner_tiles:
    for orientation in tiles[corner_tile].get_all_orientations():
      res = assemble(orientation[1].number, orientation[0])
      if res:
        return res
  return false

image_assembly, image_assembly_orientations = find_image()
image_data = ''
tile_width = tiles[corner_tiles[0]].width

# remove edges and build big image data
for i in range(0, num_tiles, image_width):
  for k in range(1, tile_width - 1):
    for j in range(0, image_width):
      image_data += tiles[image_assembly[i+j]].get_orientation(image_assembly_orientations[i+j]).data[k*tile_width + 1:(k*tile_width) + tile_width - 1]

def find_monsters(image_data):
  monster_middle_regex = re.compile('#....##....##....###')
  monster_bottom_regex = re.compile('^#..#..#..#..#..#$')
  for orientation in Tile(1, image_data).get_all_orientations():
    monster_count = 0
    for sea_monster_candidate in re.finditer('#....##....##....###', orientation[1].data):
      head_position = sea_monster_candidate.span()[0] - orientation[1].width + 18
      foot_position = sea_monster_candidate.span()[0] + orientation[1].width + 1
      if orientation[1].data[head_position] == '#' and monster_bottom_regex.match(orientation[1].data[foot_position:foot_position + 16]):
        monster_count += 1
    if monster_count > 0:
      return monster_count
  return 0

monster_count = find_monsters(image_data)
print("Task 2:", image_data.count('#') - (15 * monster_count))
