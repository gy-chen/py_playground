import numpy as np
from PIL import Image


def create_palette_random_image():
    """Play color palette image

        :return: Image object
        """
    # generate 250000 pixels with 5 random colors mapping to palette later
    pixels = np.random.randint(0, 5, 250000)
    pixels = pixels.reshape((500, 500))
    # create palette with 5 random colors
    palette = np.random.randint(0, 256, 3 * 5)
    # create color palette image
    image = Image.fromarray(pixels, 'P')
    image.putpalette(palette)
    return image


def load_image_pixels(img):
    """Get pixels of the image

        :param img: PIL image instance
        :return: numpy array that  contain pixels data and has same shape of the image
        """
    return np.asarray(img)


if __name__ == '__main__':
    image = create_palette_random_image()
    image.save('test.png')
