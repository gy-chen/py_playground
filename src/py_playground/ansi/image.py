import numpy as np
from scipy.cluster.vq import vq
from . import color, ansi

ANSI_COLOR_BOOK = [
    color.ANSIBasicColor.BLACK,
    color.ANSIBasicColor.RED,
    color.ANSIBasicColor.GREEN,
    color.ANSIBasicColor.YELLOW,
    color.ANSIBasicColor.BLUE,
    color.ANSIBasicColor.MAGENTA,
    color.ANSIBasicColor.CYAN,
    color.ANSIBasicColor.WHITE
]


def print_ansi_strings(ansi_strings):
    for line in ansi_strings:
        print(''.join(line), end=ansi.ansi_reset_string + '\n')


def convert_image_to_ansi_strings(img):
    """Convert image to ansi color string

        :param img: PIL image instance
        :return: numpy 2d array that in same size of the img. array's value in ansi string.
        """
    img = img.convert(mode='RGB')
    img_array = np.asarray(img)
    return convert_image_array_to_ansi_strings(img_array)


def convert_image_array_to_ansi_strings(img_array):
    pixels = img_array.reshape(-1, 3)
    ansi_strings = _convert_pixels_to_ansi_strings(pixels)
    return ansi_strings.reshape(img_array.shape[:2])


def _convert_pixels_to_ansi_strings(pixels):
    color_book_indexes, _ = vq(pixels, ANSI_COLOR_BOOK)
    ansi_strings = np.asarray(
        [ansi.generate_ansi_bg_color_string('　', ANSI_COLOR_BOOK[index]) for index in
         color_book_indexes])
    return ansi_strings


if __name__ == '__main__':
    from PIL import Image

    img = Image.open('t2.jpg')
    print_ansi_strings(convert_image_to_ansi_strings(img))
