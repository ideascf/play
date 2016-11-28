# coding=utf-8
# from gevent import monkey
# monkey.patch_all()

#import gevent_openssl
#gevent_openssl.monkey_patch()

from hyper import HTTP20Connection
from hyper import ssl_compat as ssl
from hyper.tls import SUPPORTED_NPN_PROTOCOLS

def gen_ssl_context():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ssl_context.set_default_verify_paths()
    # ssl_context.load_cert_chain(self.cert_file)
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.check_hostname = True
    ssl_context.set_npn_protocols(SUPPORTED_NPN_PROTOCOLS)
    # ssl_context.set_alpn_protocols(SUPPORTED_NPN_PROTOCOLS)
    ssl_context.options |= ssl.OP_NO_COMPRESSION

    return ssl_context


def f():
    c = HTTP20Connection('http2bin.org', 443, ssl_context=gen_ssl_context())
    stream_id = c.request('GET', '/bytes/10240')

    print c.get_response(stream_id).read()

if __name__ == '__main__':
    f()
