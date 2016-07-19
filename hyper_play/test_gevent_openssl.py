# coding=utf-8
from gevent import monkey
monkey.patch_all()

import test_gevent_openssl
test_gevent_openssl.monkey_patch()

from hyper import HTTP20Connection


def f():
    c = HTTP20Connection('http2bin.org', 443)
    stream_id = c.request('GET', '/bytes/10240')

    print c.get_response(stream_id).read()

if __name__ == '__main__':
    f()
