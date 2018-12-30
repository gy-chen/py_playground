"""Merge two images
"""
import argparse
from PIL import Image

parse = argparse.ArgumentParser()
parse.add_argument('images', nargs='+')


def merge(images):
    result = Image.new(images[0].mode, images[0].size, 255)
    for img in images[:]:
        mask = img.point(lambda p: p < 230 and 255)
        result.paste(img, None, mask)
    return result


def main():
    args = parse.parse_args()
    images = [Image.open(img) for img in args.images]
    merged = merge(images)
    merged.save('output.jpg')


if __name__ == '__main__':
    main()
