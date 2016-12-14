# coding=utf-8
import uuid

import os
import time
import qrcode
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
import StringIO
from concurrent import futures



background_path = './桌牌/空白桌牌.jpg'
background_paster_rgb_path = './background/rgb桌贴.jpg'
background_card_rgb_path = './background/rgb桌牌.jpg'
save_dir = '.'


# 废弃
'''
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
'''


def mix_qrcode(background_path, qr_data_str, qr_box):
    qr_box_top_x, qr_box_top_y, qr_box_width, qr_box_height = qr_box

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,
        border=1
    )

    # 背景图片
    im = Image.open(background_path)
    """:type: JpegImageFile"""
    orig_mode = im.mode  # 保存图片的原始颜色模式
    # 确保图片在操作过程中为RGB的颜色模式, CMYK的颜色模式颜色会有问题
    if orig_mode != 'RGB':
        im = im.convert('RGB')

    # 在指定像素填上二维码
    box = (qr_box_top_x, qr_box_top_y, qr_box_top_x+qr_box_width, qr_box_top_y+qr_box_height)

    # 加数据
    qr.add_data(qr_data_str)
    qr.make(fit=True)

    img_qr = qr.make_image()
    img_qr = img_qr.convert(im.mode)
    img_qr = img_qr.resize((qr_box_width, qr_box_height), Image.ANTIALIAS)

    im.paste(img_qr, box)
    target_filename = os.path.split(background_path)[1]

    # 把图片颜色模式转换为原始的颜色模式
    if im.mode != orig_mode:
        im = im.convert(orig_mode)
    im.save(os.path.join(save_dir, target_filename), 'JPEG', quality=100)



def main():
    code = '5nevG'
    url = 'https://o2.qfpay.com/prepaid/v1/page/c/recharge/index.html?h=%s' % code

    # 桌牌合成
    width_scale = 1488/357.0
    height_scale = 2079/499.0
    qr_box_top_x = int(81 * width_scale)
    qr_box_top_y = int(148 * height_scale)
    qr_box_width =  int(196 * width_scale)
    qr_box_height = int(196 * height_scale)
    card_qr_box = (qr_box_top_x, qr_box_top_y, qr_box_width, qr_box_height)
    mix_qrcode(background_card_rgb_path, url, card_qr_box)


    # 桌贴合成
    width_scale = 957/230.0
    height_scale = 1252/300.0
    qr_box_top_x = int(50 * width_scale)
    qr_box_top_y = int(85 * height_scale)
    qr_box_width =  int(130 * width_scale)
    qr_box_height = int(130 * height_scale)
    paster_qr_box = (qr_box_top_x, qr_box_top_y, qr_box_width, qr_box_height)
    mix_qrcode(background_paster_rgb_path, url, paster_qr_box)


if __name__ == '__main__':
    main()
