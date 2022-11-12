"""
Main file to launch my procedural generation project
Made by Maximilien Moriquand.
MIT license.
"""
import perlin_noise_generation
import world


def generate_map():
    """
    Generate an randomn 2d map.
    This could take a moment to render
    """
    print("===== GENERATING MAP =====")
    print("this process can be quite long (+-1mn)")
    perlin = perlin_noise_generation.Perlin(3, "", 100, 100)
    perlin.generate_simplified_noise()
    perlin.display_noise()
    myworld = world.World(100, 100)
    print("processing ...")
    myworld.generate_char_representation(perlin.raw_noise)
    myworld.as_png()
    print("the map is now saved in ~/./map/map.png")


if __name__ == "__main__":
    generate_map()
