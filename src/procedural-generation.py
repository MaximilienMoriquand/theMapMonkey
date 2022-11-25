"""
Main file to launch my procedural generation project
Made by Maximilien Moriquand.
MIT license.
"""
import perlin_noise_generation
import world
import argparse

size = 10000
output = "../map/"
input = "../tile/"


def generate_map():
    """
    Generate an randomn 2d map.
    This could take a moment to render
    """
    print("===== GENERATING MAP =====")
    print("this process can be quite long (+-1mn)")
    perlin = perlin_noise_generation.Perlin(3, "", 100, 100)
    perlin.generate_noise()
    perlin.display_noise()
    myworld = world.World(100, 100)
    print("processing ...")
    myworld.generate_char_representation(perlin.raw_noise)
    myworld.as_png()
    print("the map is now saved in ~/./map/map.png")


#
# TODO:
#       - parsing de json et class custom
#       - output file path
#       - size of the map

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MapMonkey, create a 2d map with perlin's noise")

    args = parser.parse_args()
    parser.print_help()
    generate_map()
