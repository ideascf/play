from gevent import monkey
monkey.patch_all()

import urllib2
import rsa

from tools import decorator
from tools import runner
from tools import counter

TEST_URL = 'https://www.baidu.com'
TEST_URL = 'http://127.0.0.1:9999/'
TEST_DATA = 'hello'
RSA_KEY_BITS = 1024

g_pub_key = g_pri_key = None

def _print(*args, **kwargs):
    pass
    import sys

    print(args, kwargs); sys.stdout.flush()

def make_keys():
    global  g_pub_key, g_pri_key
    g_pub_key, g_pri_key = rsa.newkeys(RSA_KEY_BITS)

    return g_pub_key, g_pri_key

cnt = 0
@decorator.qps()
@runner.ProcessRunner(5, 4)
# @runner.GeventRunner(5, 100)
def do_with_rsa():
    global cnt
    _print('BEFORE sign', cnt)
    ret_sign = rsa.sign(TEST_DATA, g_pri_key, 'SHA-1')
    _print('AFTER sign', cnt)

    _print('BEFORE urlopen', cnt)
    try:
        urllib2.urlopen(
            TEST_URL,
            TEST_DATA,
            # timeout=10
        ).read()
    except Exception as e:
        _print('IN exception', e)
        return False
    _print('AFTER urlopen', cnt)

    _print('BEFORE verify', cnt)
    rsa.verify(TEST_DATA, ret_sign, g_pub_key)
    _print('AFTER verify', cnt)

    cnt += 1

    return True

@decorator.qps()
@runner.ProcessRunner(5, 4)
# @runner.ThreadRunner(5, 100)
# @runner.GeventRunner(5, 100)
def do_no_rsa():
    global cnt

    _print('BEFORE urlopen', cnt)
    try:
        urllib2.urlopen(
            TEST_URL,
            TEST_DATA,
            # timeout=10
        ).read()
    except Exception as e:
        _print('IN exception', e)
        return False
    _print('AFTER urlopen222', cnt)

    cnt += 1

    return True

if __name__ == '__main__':
    make_keys()

    # do_with_rsa()
    do_no_rsa()