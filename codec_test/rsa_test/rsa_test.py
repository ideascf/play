import traceback

import rsa

import config


def make_keys():
    return rsa.newkeys(config.rsa_key_bits)

def test01():
    pub_key, priv_key = make_keys()

    ret_sign = rsa.sign(config.test_data, priv_key, 'SHA-1')
    rsa.verify(config.test_data, ret_sign, pub_key)

def test02():
    with open(config.public_key_file) as f:
        pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())

    with open(config.private_key_file) as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read())

    ret_sign = rsa.sign(config.test_data, priv_key, 'SHA-1')
    rsa.verify(config.test_data, ret_sign, pub_key)

def test03():
    pub_key, priv_key = make_keys()

    ret_sign = rsa.sign(config.test_data, priv_key, 'SHA-1')
    ret_sign = ret_sign.replace('a', 'A')  # damage the sign
    rsa.verify(config.test_data, ret_sign, pub_key)

if __name__ == '__main__':
    # test01()
    # test02()

    try:
        test03()
    except Exception as e:
        print(e)
        traceback.print_exc()
        traceback.print_exception()
        traceback.print_stack()
