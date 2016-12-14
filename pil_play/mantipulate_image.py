# coding=utf-8
import sys
from PIL import Image


def main():
    try:
        infile = sys.argv[1]
    except IndexError:
        infile = './ss.jpg'

    with Image.open(infile) as im:

        # 裁剪
        box = (100, 100, 400, 400)  # top_x, top_y, bottom_x, bottom_y
        region = im.crop(box)
        region.show()

        # 转换-旋转180度
        region = region.transpose(Image.ROTATE_180)
        region.show()

        # 粘贴/合成
        im.paste(region, box)
        im.show()




if __name__ == '__main__':
    main()