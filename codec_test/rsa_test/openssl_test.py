# coding=utf-8
import rsa
from OpenSSL import crypto

import config


def test():
    # 没有找到openssl的公钥加载和校验方式，所以使用rsa 的公钥和校验方式
    with open(config.public_key_file) as f:
        pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())

    with open(config.private_key_file) as f:
        priv_key = crypto.load_privatekey(crypto.FILETYPE_PEM, f.read())

    ret_sign = crypto.sign(priv_key, config.test_data, 'sha1')  # 这里的摘要算法为小写，且没有分隔符，这和rsa模块不同
    rsa.verify(config.test_data, ret_sign, pub_key)


if __name__ == '__main__':
    test()
