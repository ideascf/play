# coding=utf-8
import os
import sys
from PIL import Image


def main():
    for infile in sys.argv[1:]:
        f, e = os.path.splitext(infile)
        outfile = f + '.jpg'

        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print 'cannot convert', infile


if __name__ == '__main__':
    main()
