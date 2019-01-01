"""Merge two images
"""
import argparse
import numpy as np
from PIL import Image

parse = argparse.ArgumentParser()
parse.add_argument('images', nargs='+')


def merge(images):
    result = Image.new(images[0].mode, images[0].size, 255)
    for img in images[:]:
        mask = img.point(lambda p: p < 230 and 255)
        result.paste(img, None, mask)
    return result


def merge_np(images):
    images = [np.asarray(img) for img in images]
    result = np.min(images, axis=0)
    return Image.fromarray(result)


def main():
    args = parse.parse_args()
    images = [Image.open(img) for img in args.images]
    merged = merge_np(images)
    merged.save('output.jpg')


if __name__ == '__main__':
    main()
