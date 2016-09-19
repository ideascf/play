# coding=utf-8
import base64

import M2Crypto
import OpenSSL
from M2Crypto import SMIME, BIO, X509
signkey = "test"  # 签名key，测试环境测试的都是test，生产上一个会员对应一个key
passWord = "111111" # 测试秘钥文件密码，随同pfx证书一起的密码
pri = "./rsa/server.pfx" # 测试秘钥文件名（该文件包含公钥和私钥）外部商户请更换申请的pfx证书
pub = "./rsa/npp_11_API2test.pem" # 代付证书文件名

data  = 'biz_trade_no=2015003456&category_code=20jd22022&customer_no=360080002191800017&extend_params={"ssss":"ssss"}&notify_url=http://test/&out_trade_date=20150519T103700&out_trade_no=23456587692&pay_tool=TRAN&payee_account_name=张米克&payee_account_no=6222600210011817312&payee_account_type=P&payee_bank_code=ABC&payee_bank_fullname=农业银行&payee_card_type=DE&payee_mobile=1333333333&request_datetime=20150519T103700&return_params=1234ssddffgghhj&seller_info={customer_code:"360080002191800017",customer_type:"CUSTOMER_NO"}&trade_amount=1&trade_currency=CNY&trade_source=testetst&trade_subject=test代付'

pri_content = open(pri).read()
certs = OpenSSL.crypto.load_pkcs12(pri_content, passWord)
sign_cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, certs.get_certificate())
sign_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, certs.get_privatekey())


encry_cert = open(pub).read()

smime = SMIME.SMIME()

# smime.load_key(
#     keyfile=pri,
#     certfile=pub
# )
smime.load_key_bio(
    keybio=BIO.MemoryBuffer(sign_key),
    certbio=BIO.MemoryBuffer(sign_cert)
)
data_bio = BIO.MemoryBuffer(data)


p7 = smime.sign(data_bio, SMIME.PKCS7_NOATTR|SMIME.PKCS7_BINARY|SMIME.PKCS7_NOSIGS)

out = BIO.MemoryBuffer()
smime.write(out, p7)
ret = out.read()
base64_sign = ret[ret.index('base64') + len('base64'):]
base64_sign = base64_sign.strip()
print base64_sign
raw_sign = base64.b64decode(base64_sign)

print '\n\n'
print '++++'*10
print '\n\n'

x509 = X509.load_cert(pub)
sk = X509.X509_Stack()
sk.push(x509)
#
# 'des_cbc',
# 'des_cfb',
# 'des_ecb',
# 'des_ede3_cbc',
# 'des_ede3_cfb',
# 'des_ede3_ecb',
# 'des_ede3_ofb',
# 'des_ede_cbc',
# 'des_ede_cfb',
# 'des_ede_ecb',
# 'des_ede_ofb',
# 'des_ofb',

smime = SMIME.SMIME()
smime.set_x509_stack(sk)
smime.set_cipher(SMIME.Cipher('des_ede3_cbc'))
# smime.set_cipher(SMIME.Cipher('des_ede3_cfb'))
# smime.set_cipher(SMIME.Cipher('des_ede3_ecb'))
# smime.set_cipher(SMIME.Cipher('des_ede3_ofb'))

p7 = smime.encrypt(BIO.MemoryBuffer(raw_sign), flags=SMIME.PKCS7_BINARY)


# tmp = BIO.MemoryBuffer()
# # smime.write(tmp, p7, data_bio, flags=SMIME.PKCS7_BINARY)
# p7 = smime.encrypt(tmp)



out = BIO.MemoryBuffer()
smime.write(out, p7)
ret = out.read()
base64_envelope = ret[ret.index('base64') + len('base64'):]
base64_envelope = base64_envelope.strip()
base64_envelope = base64.b64encode(base64.b64decode(base64_envelope))
print base64_envelope

# envelope = smime.encrypt(BIO.MemoryBuffer(data), SMIME.PKCS7_BINARY|1)
# print envelope
