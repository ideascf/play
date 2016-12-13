# coding=utf-8
import os
import time
import qrcode
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
import StringIO
from concurrent import futures



background_path = './桌牌/空白桌牌.jpg'
save_dir = '.'


def create_qrcode(code):
    width_scale = 1488/357.0
    height_scale = 2079/499.0

    qr_box_top_x = int(81 * width_scale)
    qr_box_top_y = int(148 * height_scale)
    qr_box_width =  int(196 * width_scale)
    qr_box_height = int(196 * height_scale)

    # qr
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,
        border=1
    )

    # 背景图片
    im = Image.open(background_path)
    print im
    """:type: JpegImageFile"""
    # dpi = im.info['dpi']

    # 在指定像素填上二维码
    box = (qr_box_top_x, qr_box_top_y, qr_box_top_x+qr_box_width, qr_box_top_y+qr_box_height)

    # 加数据
    qr.add_data('https://o2.qfpay.com/prepaid/v1/page/c/recharge/index.html?h=%s' % code)
    qr.make(fit=True)

    img_qr = qr.make_image()
    img_qr = img_qr.convert("RGBA")
    img_qr = img_qr.resize((qr_box_width, qr_box_height), Image.ANTIALIAS)

    im.paste(img_qr, box)
    # im.save(StringIO.StringIO())
    im.save(os.path.join(save_dir, '%s.jpg' % code), 'JPEG', quality=100)



def main():
    create_qrcode('5nevG')


if __name__ == '__main__':
    main()
