"""
This file contains all the world's attribute as it should be generated.
"""


def translate_noise_tile_id(value):
    if -0.2 > value:  # i fucking love python
        return 11  # deep water
    elif -0.2 <= value < 0:
        return 12  # lake water
    elif 0.4 < value:
        return 21  # rock
    elif 0 <= value < 0.1:
        return 22  # sand
    elif 0.1 <= value < 0.2:
        return 24  # dirt
    elif 0.2 <= value < 0.4:
        return 23  # grass


def translate_noise_char(value):
    if -0.2 > value:  # i fucking love python
        return "Wd"  # deep water
    elif -0.2 <= value < 0:
        return "Wl"  # lake water
    elif 0.4 < value:
        return "Gr"  # rock
    elif 0 <= value < 0.1:
        return "Gs"  # sand
    elif 0.1 <= value < 0.2:
        return "Gd"  # dirt
    elif 0.2 <= value < 0.4:
        return "Gg"  # grass


class World:
    """
    class World:
        - width (int) = the width of the world
        - height (int) = the height of the world
        - char_representation = the matrix of char that represent the world (see Tile class)
        - tile_id_representation = the matrix of tile_id that represent the wolrd (see Tile class)
        - dico_tile = a dictionnary to get the Tile from an tile_id
        - seed (string) = a unique string that define the world.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.char_representation = []
        self.tile_id_representation = []
        self.dico_tile = {}
        self.seed = "To be defined"

    def print_char_world(self):
        for i in self.char_representation:
            print(i)

    def print_id_tile_world(self):
        for i in self.tile_id_representation:
            print(i)

    def print_world_data(self):
        print("=== WORLD ===")
        print("   - width: " + str(self.width))
        print("   - height: " + str(self.height))
        print("   -- CHAR RPZ --")
        self.print_char_world()
        print("   -- ID RPZ --")
        self.print_id_tile_world()
        print("   - seed : " + str(self.seed))
        print("==============")

    def generate_tile_id_representation(self, perlin_noice):
        for line in perlin_noice:
            add_me = []
            for element in line:
                add_me.append(translate_noise_tile_id(element))
            self.tile_id_representation.append(add_me)

    def generate_char_representation(self, perlin_noice):
        for line in perlin_noice:
            add_me = []
            for element in line:
                add_me.append(translate_noise_char(element))
            self.char_representation.append(add_me)

