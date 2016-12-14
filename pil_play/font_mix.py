# coding=utf-8
import qrcode
import datetime
from PIL import Image, ImageFont, ImageDraw, ImageColor
from PIL.JpegImagePlugin import JpegImageFile


background_cmyk_path = './background/cmyk海报.jpg'
background_rgb_path = './background/rgb海报.jpg'

font1_path = './font/造字工房尚黑G0v1粗体.otf'
font2_path = './font/Lantinghei.ttc'
activity_dict = {
    'start_date': datetime.date(2016, 12, 7),
    'end_date': datetime.date(2017, 1, 7),
    'rules': [
        {
            'pay_amt': 10000,
            'present_amt': 3000,
        },
        {
            'pay_amt': 30000,
            'present_amt': 8000,
        },
        {
            'pay_amt': 500000,
            'present_amt': 12000,
        },
        {
            'pay_amt': 900000,
            'present_amt': 28000,
        },
    ],
    'copyright_notice': '最终解释权归QQ堂所有',
}


def center_text(text_str, font, target_box):
    """

    :param text_str:
    :param font:
    :param target_box: (x, y, width, height)
    :type text_str:
    :type font: ImageFont.ImageFont
    :type target_box: tuple
    :return:
    :rtype:
    """

    text_w, text_h = font.getsize(text_str)
    box_w, box_h = target_box[2:]
    box_x, box_y = target_box[:2]

    top_x = box_x + (box_w - text_w)/2
    top_y = box_y + (box_h - text_h)/2

    return top_x, top_y


def text_horizon_center(text, font, target_pos_x, target_width):
    text_w, _ = font.getsize(text)

    top_x = target_pos_x + (target_width - text_w)/2

    return top_x


def text_vertical_center(text, font, target_pos_y, target_height):
    _, text_h = font.getsize(text)

    top_y = target_pos_y + (target_height - text_h)/2

    return top_y


rgb_scale = 255
cmyk_scale = 100


def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, cmyk_scale

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / float(rgb_scale)
    m = 1 - g / float(rgb_scale)
    y = 1 - b / float(rgb_scale)

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy)
    m = (m - min_cmy)
    y = (y - min_cmy)
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    # return c*cmyk_scale, m*cmyk_scale, y*cmyk_scale, k*cmyk_scale
    ret = (c*cmyk_scale, m*cmyk_scale, y*cmyk_scale, k*cmyk_scale)
    return tuple(int(i) for i in ret)


def cmyk_to_rgb(c,m,y,k):
    """
    """
    r = rgb_scale*(1.0-(c+k)/float(cmyk_scale))
    g = rgb_scale*(1.0-(m+k)/float(cmyk_scale))
    b = rgb_scale*(1.0-(y+k)/float(cmyk_scale))
    return r,g,b


def mix(background_path, activity_dict, code):
    """
    1. 出现的pos,不做特殊说明时, 均代表左上角坐标
    2. 文档中标注的PX,均需要乘上scale得到实际的像素值
    3. 目前只支持RGB/RGBA格式的合成
    """

    width_scale = 5031/1207.0
    height_scale = 6803/1633.0

    start_date = activity_dict['start_date']
    end_date = activity_dict['end_date']
    rules = activity_dict['rules']
    copyright_notice = activity_dict['copyright_notice']

    im = Image.open(background_path)
    """:type: JpegImageFile"""
    draw = ImageDraw.Draw(im, im.mode)


    date_str_font_size = int(width_scale * 35)  # 活动时间字符串的字体大小
    date_str_font = ImageFont.truetype(font1_path, date_str_font_size)
    date_color = '#8A5D3B'

    dot_font_size = int(width_scale * 14)  # 原点尺寸: 14PX
    dot_font = ImageFont.truetype(font2_path, dot_font_size)
    dot_color = '#F7913C'

    rule_font_size = int(width_scale * 60)  # 储值规则文字尺寸: 60PX
    rule_font = ImageFont.truetype(font1_path, rule_font_size)
    rule_color = '#8A5D3B'

    amt_font_size = int(width_scale * 65)  # 储值规则中金额文字尺寸: 65PX
    # index=2, 选择: 'Lantinghei SC', 'Heavy' 字体
    amt_font = ImageFont.truetype(font2_path, amt_font_size, index=2)
    amt_font_height_padding = amt_font_size / 5
    pay_amt_color = '#8A5D3B'
    present_amt_color = '#FD5359'
    pay_amt_width = int(width_scale * 248)  # 支付金额宽度: 248PX
    present_amt_width = int(width_scale * 180)  # 赠送金额宽度: 180PX

    copyright_notice_font_size = int(width_scale * 25)  # 最终解释权文字尺寸: 25PX
    # index=2, 选择: 'Lantinghei SC', 'Heavy' 字体
    copyright_notice_font = ImageFont.truetype(font2_path, copyright_notice_font_size, index=2)
    copyright_notice_color = '#8A5D3B'


    #### 绘制时间字符串 ####
    date_str = u'%s月%s日-%s月%s日' % (start_date.month, start_date.day, end_date.month, end_date.day)
    w, h = draw.textsize(date_str, date_str_font)  # 可通过此方法得到date_str 的实际像素box
    date_str_pos = (2300, 2050)  # 活动时间字符串的起始位置,  @IMPORTANT 请按实际计算得到
    draw.text(
        date_str_pos,   #
        date_str,
        fill=date_color,
        font=date_str_font,
    )


    #### 绘制储值规则 #####
    # 规则字符串的起始位置,  @IMPORTANT 请按实际计算得到
    rule_line_text_height = rule_font.getsize(u'储值')[1] # 每行储值规则文字的高度
    rule_str_pos = (1000, 2600)
    cur_x, cur_y = rule_str_pos
    for rule in activity_dict['rules']:
        # 绘制圆点
        draw.text(
            (cur_x, text_vertical_center(u'●', dot_font, cur_y, rule_line_text_height)),
            u'●',
            fill=dot_color,
            font=dot_font
        )
        cur_x += dot_font.getsize(u'●')[0]

        # 圆点和文字之间间隔28PX
        cur_x += (width_scale * 28)

        # 绘制 '储值'  二字
        draw.text(
            (cur_x, cur_y),
            u'储值',
            fill=rule_color,
            font=rule_font,
        )
        cur_x += rule_font.getsize(u'储值')[0]

        # 绘制 支付金额
        pay_amt_text = u'{}'.format(rule['pay_amt']/100)  # 单位转为: 元
        draw.text(
            (text_horizon_center(pay_amt_text, amt_font, cur_x, pay_amt_width), cur_y-amt_font_height_padding),  # 兰亭字体height有padding
            pay_amt_text,
            fill=pay_amt_color,
            font=amt_font,
        )
        cur_x += pay_amt_width


        # 绘制 '元送'  二字
        draw.text(
            (cur_x, cur_y),
            u'元送',
            fill=rule_color,
            font=rule_font,
        )
        cur_x += rule_font.getsize(u'元送')[0]

        # 绘制赠送金额
        present_amt_text = u'{}'.format(rule['present_amt'] / 100)  # 单位转为: 元
        draw.text(
            (text_horizon_center(present_amt_text, amt_font, cur_x, present_amt_width), cur_y-amt_font_height_padding),  # 兰亭字体height有padding
            present_amt_text,
            fill=present_amt_color,
            font=amt_font,
        )
        cur_x += present_amt_width

        # 绘制 '元' 字
        draw.text(
            (cur_x, cur_y),
            u'元',
            fill=rule_color,
            font=rule_font,
        )
        cur_x += rule_font.getsize(u'元')[0]

        # 下一行
        cur_x = rule_str_pos[0]
        cur_y += (height_scale * 40) + rule_font.getsize(u'储值')[1]  # 规则上下行距40PX + 文字高度


    #### 绘制最终解释权文案 ####
    # 绘制圆点
    s = activity_dict['copyright_notice']
    copyright_notice_str = s if isinstance(s, unicode) else s.decode('utf8')
    copyright_notice_text_height = copyright_notice_font.getsize('文字')[1]

    draw.text(
        (cur_x, text_vertical_center(u'●', dot_font, cur_y, copyright_notice_text_height)),
        u'●',
        fill=dot_color,
        font=dot_font
    )
    cur_x += dot_font.getsize(u'●')[0]

    # 圆点和文字之间间隔28PX
    cur_x += (width_scale * 28)

    # 绘制最终解释权文字
    draw.text(
        (cur_x, cur_y),
        copyright_notice_str,
        fill=copyright_notice_color,
        font=copyright_notice_font
    )

    # 测试兰亭字体height的padding
    # draw.text(
    #     (0, 0),
    #     u'测试',
    #     fill=pay_amt_color,
    #     font=ImageFont.truetype(font2_path, 150, index=2),
    # )
    # h = 30
    # draw.line((0, h, 1000, h), fill='black', width=1)


    #### 绘制二维码 ####
    qr_box_top_x = int(550 * width_scale)
    qr_box_top_y = int(1136 * height_scale)
    qr_box_width =  int(147 * width_scale)
    qr_box_height = int(147 * height_scale)

    # qr
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,
        border=1
    )

    # 在指定像素填上二维码
    box = (qr_box_top_x, qr_box_top_y, qr_box_top_x+qr_box_width, qr_box_top_y+qr_box_height)

    # 加数据
    qr.add_data('https://o2.qfpay.com/prepaid/v1/page/c/recharge/index.html?h=%s' % code)
    qr.make(fit=True)

    img_qr = qr.make_image()
    img_qr = img_qr.convert(im.mode)
    img_qr = img_qr.resize((qr_box_width, qr_box_height), Image.ANTIALIAS)
    im.paste(img_qr, box)

    ##### 保存 #####
    target_filename = '{code}_{mode}.jpg'.format(code=code, mode=im.mode)
    im.save(target_filename, 'JPEG', quality=100)


def main():
    mix(background_rgb_path, activity_dict, '5nevG')
    # mix(background_cmyk_path, activity_dict, '5nevG')


if __name__ == '__main__':
    main()