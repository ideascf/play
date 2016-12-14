# coding=utf-8
import sys
from PIL import Image

def main():
    for infile in sys.argv[1:]:
        try:
            with Image.open(infile) as im:
                print infile, im.format, "%dx%d" % im.size, im.mode
        except IOError:
            pass


if __name__ == '__main__':
    main()
