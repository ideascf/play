import base64
import binascii

def equal():
    for i in range(256):
        c = chr(i)

        # 这两种编码方式几乎是一样的，除了得到的结果的大小写不同。
        # 这两种编码方式得到的结果都是偶数字节长度， 故当解码时传入的长度不为偶数时，会抛出 'TypeError: Odd-length string'
        #
        a = base64.b16encode(c)  # Got upper-case
        b = binascii.hexlify(c)  # Got lower-case, Almost equal base64.b16encode

        print c, a, b, a.upper() == b.upper()

def other():
    for i in range(256):
        c = chr(i)

        x = base64.b32encode(c)
        y = base64.b64encode(c)

        print c, x, y

if __name__ == '__main__':
    equal()
    other()

