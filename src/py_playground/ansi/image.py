import numpy as np
from scipy.cluster.vq import vq
from . import color, ansi

ANSI_COLOR_BOOK = [
    color.Color.BLACK,
    color.Color.RED,
    color.Color.GREEN,
    color.Color.YELLOW,
    color.Color.BLUE,
    color.Color.MAGENTA,
    color.Color.CYAN,
    color.Color.WHITE
]


def convert_image_to_ansi_strings(img):
    """Convert image to ansi color string

        :param img: PIL image instance
        :return: string
        """
    img = img.convert(mode='RGB')
    img_array = np.asarray(img)
    return convert_image_array_to_ansi_strings(img_array)


def convert_image_array_to_ansi_strings(img_array):
    ansi_strings = _convert_pixels_to_ansi_strings(img_array)
    return ansi_strings


def _convert_pixels_to_ansi_strings(pixels):
    original_shape = pixels.shape
    pixels = pixels.reshape(-1, 3)
    color_book_indexes, _ = vq(pixels, ANSI_COLOR_BOOK)
    ansi_strings = np.asarray(
        [ansi.generate_ansi_color_string(' ', color.get_ansi_bg_code(ANSI_COLOR_BOOK[index])) for index in
         color_book_indexes]).reshape(
        original_shape[:2])
    return ansi_strings


if __name__ == '__main__':
    from PIL import Image

    img = Image.open('t2.jpg')
    ansi_strings = convert_image_to_ansi_strings(img)
    for line in ansi_strings:
        print(''.join(line))
