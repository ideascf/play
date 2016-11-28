# coding=utf-8
import os
import time
import qrcode

from yyk import codes

from functools import wraps
from PIL import Image
from tqdm import tqdm
from concurrent import futures

# 判断是否是一个有效的日期字符串
def is_valid_date(s, fmt='%Y%m%d'):
    try:
        time.strptime(s, fmt)
        return True
    except:
        return False

# 装饰器
def dd(func):
    @wraps(func)
    def wrap(*args):
        if env == 'test':
            if not os.path.exists('test'):
                os.mkdir('test')
            return func()

        # 创建test目录
        if os.path.exists('test'):
            os.system('rm -fr test')
        else:
            os.mkdir('test')

        ret = func(*args)

        # 移动目录
        dirs = os.listdir('./')
        dirs = [i for i in dirs if is_valid_date(i)]
        # 删除目录
        tddir = time.strftime('%Y%m%d')
        if tddir not in dirs:
            os.system('rm -fr {rmdirs};mv test {tddir}'.format(rmdirs=' '.join(dirs), tddir=tddir))
        else:
            tddirs = os.listdir(tddir)
            tddirs = [int(i) for i in tddirs if i.isalnum()]
            if not tddirs:
                os.system('mv {tddir} 1;mkdir {tddir};mv 1 {tddir}'.format(tddir=tddir))
            nowdir = '%s/%s' % (tddir, max(tddirs or [1]) + 1)
            os.system('mv test {nowdir}'.format(nowdir=nowdir))

        return ret

    return wrap

def create_qrcode(code):
    size = 800
    path = 'test'

    # qr
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,
        border=1
    )

    # 背景图片
    im = Image.open('bg.png')
    dpi = im.info['dpi']

    # 在指定像素填上二维码
    left, top = 280, 30
    box = (left, top, left+size, top+size)

    # 加数据
    qr.add_data('https://o2.qfpay.com/qr/%s' % code)
    qr.make(fit=True)

    img_qr = qr.make_image()
    img_qr = img_qr.convert("RGBA")
    img_qr = img_qr.resize((size, size), Image.ANTIALIAS)

    im.paste(img_qr, box)
    #im.save('./%s/%s.png' % (path, code))
    im.save('./%s/%s.png' % (path, code), 'png', quality=100, dpi=dpi)



@dd
def main():
    ccodes =  ['yyk'] if env == 'test' else codes

    #with futures.ProcessPoolExecutor() as exe:
    with futures.ThreadPoolExecutor(10) as exe:
        for i in tqdm(exe.map(create_qrcode, ccodes), total = len(ccodes)):pass

if __name__ == '__main__':
    main()
