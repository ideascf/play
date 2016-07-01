# coding:utf-8
"""
本代码的目的是测试gevent的ssl模块：

当monkey.patch中对ssl模块打patch，是否导致gevent不能异步。

"""
from gevent import monkey
#monkey.patch_all(ssl=False)
monkey.patch_all()


import gevent
import requests

def foo():
    print 'start ....'

    resp = requests.get('https://www.baidu.com')

    print resp.content


if __name__ == '__main__':
    g1 = gevent.spawn(foo)
    g2 = gevent.spawn(foo)


    gevent.joinall([g1, g2])

    print 'finish all.'
