import rsa
import gevent
import time
import functools

from tools import decorator
import config

RSA_KEY_BYTES = 1024
# RSA_KEY_BYTES = 2048
pub_key = None
pri_key = None

import logging
import sys
decorator.profile_log.addHandler(
    logging.StreamHandler(sys.stdout)
)
decorator.profile_log.setLevel('INFO')


def make_key():
    global pub_key, pri_key

    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(open(config.pub_key_file).read())
    pri_key = rsa.PrivateKey.load_pkcs1(open(config.priv_key_file).read())

def do():
    s = 'hello'
    ret_sign = rsa.sign(s, pri_key, 'SHA-1')
    rsa.verify(s, ret_sign, pub_key)

@decorator.timeit
def main():
    for _ in range(config.calc_times):
        do()

if __name__ == '__main__':
    make_key()

    main()
