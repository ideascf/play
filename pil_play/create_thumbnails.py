# coding=utf-8
import os
import sys
from PIL import Image


size = (128, 128)


def main():
    for infile in sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + '.thumbnail'
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size)
                im.save(outfile, "JPEG")
            except IOError:
                print 'cannot create thumbnail for ', infile


if __name__ == '__main__':
    main()
