# coding=utf-8

import sys
from PIL import Image



def roll(image, delta):
    "roll an image sideways"

    xsize, ysize = image.size
    delta = delta % xsize
    if delta == 0:
        return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image

def main():
    try:
        infile = sys.argv[1]
    except IndexError:
        infile = './ss.jpg'

    with Image.open(infile) as im:
        roll(im, 500).show()


if __name__ == '__main__':
    main()