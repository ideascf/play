import Crypto
from Crypto.Signature import PKCS1_v1_5 as pkcs
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

import config

def load_keys():
    with open(config.public_key_file) as f:
        pub_key = RSA.importKey(f.read())

    with open(config.private_key_file) as f:
        priv_key = RSA.importKey(f.read())

    return pub_key, priv_key

def main():
    pub_key, priv_key = load_keys()

    d = SHA.new(config.test_data)

    priv = pkcs.new(priv_key)
    ret_sign = priv.sign(d)

    pub = pkcs.new(pub_key)
    pub.verify(d, ret_sign)


if __name__ == '__main__':
    main()
