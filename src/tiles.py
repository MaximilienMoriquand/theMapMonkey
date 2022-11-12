"""
This file contains all class's tiles definition
A tile can be considered as unit of display (eg a big pixel) or a patch of land/water in a world.
"""
from os.path import exists





"""
Main class for tile, generic from wich every other tiles will ihnerit

        - id : int, must be an unique id
        - size: int, must be > 0
        - image_path: string, if the path is incorrect a default path will be added.
        - coord: the coordonate on the grid.
        - char : the string that represent the tile, usually [TYPE][first letter] => deep water == Wd
        - color : if the image is not found, it will be replaced by [image].png on the picture.
"""


class Tile:
    def __init__(self, id, size, image_path, coord, color):
        self.id = id
        self.class_id = -1  # value to immediately know which class is the tile.
        self.char = "U"
        self.size = size
        if exists(image_path):
            self.image_path = image_path
        else:
            self.image_path(char + ".png")
        self.coord = coord
        self.color = color

    def print_metadata(self):
        print("=== Tile : " + self.id + " ===")
        print("   - size : " + str(self.size))
        print("   - image_path : " + str(self.image_path))
        print("   - coord : " + str(self.coord))
        print("   - color : " + str(self.color))
        print("   - class_id: " + str(self.class_id))


"""
========================= Specific tiles =======================

Those are my (rather simple) implementation of a terrain tiles.
Each of them have a class id ( following the hotel way of giving id) and a string that represent them.
I plan to add 'affinity matrix' in each class to modify the chance of getting a tile for a neighboor:
    - the sand should be more likely be between water and dirt
    - deepwater must be near lakewater 
    - ... 

"""

"""

Water Tile, general one from wich all the water type will inherent.

"""


class WaterTile(Tile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "blue")
        self.class_id = 1
        self.char = "W"


class WaterDeepTile(WaterTile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "deep_blue")
        self.class_id = 11
        self.char = "Wd"


class WaterLakeTile(WaterTile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "light_blue")
        self.class_id = 12
        self.char = "Wl"


"""

Ground Tile, general one from wich all the ground type will inherent.

"""


class GroundTile(Tile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "black")
        self.class_id = 2
        self.char = "G"


class GroundRockTile(GroundTile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "grey")
        self.class_id = 21
        self.char = "Gr"


class GroundSandTile(GroundTile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "yellow")
        self.class_id = 22
        self.char = "Gs"


class GroundGrassTile(GroundTile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "green")
        self.class_id = 23
        self.char = "Gg"


class GroundDirtTile(GroundTile):
    def __init__(self, id, size, image_path, coord):
        super().__init__(id, size, image_path, coord, "brown")
        self.class_id = 24
        self.char = "Gd"
