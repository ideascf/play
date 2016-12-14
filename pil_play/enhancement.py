# coding=utf-8
from __future__ import  print_function
import sys
from PIL import Image, ImageFilter, ImageEnhance


def main():
    try:
        infile = sys.argv[1]
    except IndexError:
        infile = './ss.jpg'

    with Image.open(infile) as im:
        im.filter(ImageFilter.DETAIL).show()

        # split the image into individual bands
        source = im.split()
        R, G, B = 0, 1, 2
        # select regions where red is less than 100
        mask = source[R].point(lambda i: i < 100 and 255)
        # process the green band
        out = source[G].point(lambda i: i * 0.7)
        # paste the processed band back, but only where red was < 100
        source[G].paste(out, None, mask)
        # build a new multiband image
        im = Image.merge(im.mode, source)
        im.show()


        enh = ImageEnhance.Contrast(im)
        enh.enhance(1.3).show("30% more contrast")



if __name__ == '__main__':
    main()