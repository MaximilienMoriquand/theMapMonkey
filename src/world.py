"""
This file contains all the world's attribute as it should be generated.
"""
import random

import cv2
from os.path import exists
import os
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

    def as_png(self):
        if(self.char_representation==[]):
            raise Exception("the char representation is empty")
            exit(405)
        image_path = "../tiles/U.png"
        print(os.getcwd())
        first_row=True
        final_image=cv2.imread("../tiles/U.png")
        if exists(image_path):
            for i in self.char_representation:
                row=""
                first=True
                for charcode in i:
                    print(charcode)
                    if first:

                        row= cv2.imread("../tiles/"+charcode+".png")
                        row= cv2.resize(row, dsize=(0, 0),
                                            fx=0.01, fy=0.01)
                        first=False
                        print("first of the row")
                    else:
                        img1 = cv2.imread("../tiles/"+charcode+".png")
                        img1_s = cv2.resize(img1, dsize=(0, 0),
                                            fx=0.01, fy=0.01)
                        row = cv2.hconcat([row, img1_s])

                if first_row:
                    final_image = row
                    first_row=False
                else:
                    final_image=cv2.vconcat([final_image,row])
            cv2.imwrite('../map/map.png',final_image)
        else:
            print("the file does not exist, please check the content of ../tiles/")