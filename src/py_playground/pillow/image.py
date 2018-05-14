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


def resize_image(img, new_width=None, new_height=None):
    return img.resize(get_image_resize_size(img, new_width, new_height))


def get_image_resize_size(img, new_width=None, new_height=None):
    if new_width is None and new_height is None:
        return img.size
    if new_width is not None and new_height is not None:
        return new_width, new_height
    if new_width is not None:
        ratio = _get_ratio(img.size[0], new_width)
        new_height = _apply_ratio(ratio, img.size[1])
        return new_width, new_height
    if new_height is not None:
        ratio = _get_ratio(img.size[1], new_height)
        new_width = _apply_ratio(ratio, img.size[0])
        return new_width, new_height


def _get_ratio(old_value, new_value):
    return new_value / old_value


def _apply_ratio(ratio, value):
    return int(ratio * value)


if __name__ == '__main__':
    #image = create_palette_random_image()
    #image.save('test.png')

    image = Image.open('t1.jpg')
    resized_image = resize_image(image, 100)
    resized_image.save('t2.jpg')
