# coding=utf-8
import sys
from PIL import Image


def main():
    try:
        infile = sys.argv[1]
    except IndexError:
        infile = './ss.jpg'

    with Image.open(infile) as im:
        im.convert("L").show()
        im.convert("CMYK").show()



if __name__ == '__main__':
    main()