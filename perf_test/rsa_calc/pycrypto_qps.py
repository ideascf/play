from Crypto.Signature import PKCS1_v1_5 as pkcs
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import config
from tools import perf

perf.set_profile_log()
pub_key = priv_key = None

def load_keys():
    global pub_key, priv_key

    with open(config.pub_key_file) as f:
        pub_key = RSA.importKey(f.read())

    with open(config.priv_key_file) as f:
        priv_key = RSA.importKey(f.read())

    return pub_key, priv_key

@perf.timeit
def main():
    def do(pub_key, priv_key):
        d = SHA.new('hello')

        priv = pkcs.new(priv_key)
        ret_sign = priv.sign(d)

        pub = pkcs.new(pub_key)
        pub.verify(d, ret_sign)

    for _ in range(config.calc_times):
        do(pub_key, priv_key)

@perf.timeit
def main_01():
    def do(pub, priv):
        d = SHA.new('hello')

        ret_sign = priv.sign(d)
        pub.verify(d, ret_sign)

    pub = pkcs.new(pub_key)
    priv = pkcs.new(priv_key)

    for _ in range(config.calc_times):
        do(pub, priv)


if __name__ == '__main__':
    load_keys()

    main()
    # main_01()
