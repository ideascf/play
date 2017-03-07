# coding=utf-8
import json

from gevent import monkey
monkey.patch_all(subprocess=True)


import gevent
import subprocess


d = {
    'h': '啊',
    'b': 123
}

def work(delay):
    subprocess.call(['/bin/sleep', str(delay)])
    subprocess.call(['/home/cf/py2_vir/bin/python', '/home/cf/code/python/play/gevent_test/echo.py', json.dumps(d), 'h h h h h'])
    print delay, 'finish...'


def main():
    l = [
        gevent.spawn(work, i)
        for i in range(10, 0, -1)
    ]

    gevent.joinall(l)
    print 'ALL finish'

if __name__ == '__main__':
    main()
