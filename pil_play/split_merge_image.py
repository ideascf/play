# coding=utf-8
from PIL import Image
import sys


def main():
    try:
        infile = sys.argv[1]
    except IndexError:
        infile = './ss.jpg'

    with Image.open(infile) as im:
        r, g, b = im.split()
        r.show(); g.show(); b.show()

        im = Image.merge('RGB', (r, g, b))
        im.show()


if __name__ == '__main__':
    main()