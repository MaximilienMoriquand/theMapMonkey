"""
Using Perlin noise to generate a layout map.

Inspired from those cool article :
    - http://adrianb.io/2014/08/09/perlinnoise.html
    - https://samclane.dev/Perlin-Noise-Python/
Using this librairy: https://github.com/salaxieb/perlin_noise
"""
import perlin_noise
import matplotlib.pyplot as plt


class Perlin:
    """
    octave = the number of interpolation
    seed = (need implemantation) the seed for the rng
    xpix = max x of the array containing the noise
    ypix = max y of the array containing the noise
    raw_noise = the raw data extracted from the noise
    image_plot = used to display an image of the noise
    """

    def __init__(self, octave, seed, xpix, ypix):
        self.octave = octave
        self.seed = seed
        self.xpix = xpix
        self.ypix = ypix
        self.raw_noise = []
        self.image_plot = 0
        """
        translation tables to convert the value in the raw noises to a tile
        see class_id in the classes in tiles.py
        """

    def generate_noise(self):
        """
        largely inspired from the documentation  https://github.com/salaxieb/perlin_noise
        stored the resulting noice in the feild named "raw_noise"
        """
        noise1 = perlin_noise.PerlinNoise(octaves=3)
        noise2 = perlin_noise.PerlinNoise(octaves=6)
        noise3 = perlin_noise.PerlinNoise(octaves=12)
        noise4 = perlin_noise.PerlinNoise(octaves=24)
        pic = []
        for i in range(self.xpix):
            row = []
            for j in range(self.ypix):
                noise_val = noise1([i / self.xpix, j / self.ypix])
                noise_val += 0.5 * noise2([i / self.xpix, j / self.ypix])
                noise_val += 0.25 * noise3([i / self.xpix, j / self.ypix])
                noise_val += 0.125 * noise4([i / self.xpix, j / self.ypix])

                row.append(noise_val)
            pic.append(row)
        self.raw_noise = pic

    def display_noise(self):
        """
        using matplotlib to display an image extracted from the raw data of the noise.
        """
        self.image_plot = plt.imshow(self.raw_noise)
        plt.colorbar()
        plt.show()
