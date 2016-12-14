# coding=utf-8
from PIL import Image
import sys


def main():
    try:
        infile = sys.argv[1]
    except IndexError:
        infile = './ss.jpg'

    with Image.open(infile) as im:
        im.resize((256, 256)).show()  # 缩放

        im.rotate(45).show()  # 旋转

        im.transpose(Image.FLIP_LEFT_RIGHT).show()
        im.transpose(Image.FLIP_TOP_BOTTOM).show()
        im.transpose(Image.ROTATE_90).show()
        im.transpose(Image.ROTATE_180).show()
        im.transpose(Image.ROTATE_270).show()


if __name__ == '__main__':
    main()