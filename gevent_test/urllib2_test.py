from gevent import monkey
monkey.patch_all()

import gevent
import urllib2

def main():
    print('before urlopen...')
    resp = urllib2.urlopen('http://www.baidu.com')
    print('after urlopen...')
    ret = resp.read()
    print('after read...')
    print(ret)

if __name__ == '__main__':
    gevent.joinall(
        [
            gevent.spawn(main)
            for i in range(10)
        ]
    )
