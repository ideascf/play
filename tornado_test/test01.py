import rsa
import sys
from tornado import web, ioloop

g_pri_key = g_pub_key = None
g_with_rsa = True
g_with_rsa = False
g_cnt = 0
RSA_KEY_BITS = 1024
TEST_DATA = 'hello'


def make_keys():
    global g_pub_key, g_pri_key
    g_pub_key, g_pri_key = rsa.newkeys(RSA_KEY_BITS)

    return g_pub_key, g_pri_key

class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello')
        self._dumy()

    def post(self, *args, **kwargs):
        self.write('hello')
        self._dumy()

    def _dumy(self):
        global g_with_rsa, g_cnt

        g_cnt += 1
        # print(g_cnt)

        if g_with_rsa:
            ret_sign = rsa.sign(TEST_DATA, g_pri_key, 'SHA-1')
            rsa.verify(TEST_DATA, ret_sign, g_pub_key)


app = web.Application(
    [
        ('/', MainHandler)
    ]
)

if __name__ == '__main__':
    make_keys()

    port = int(sys.argv[1])
    app.listen(port)

    ioloop.IOLoop.instance().start()
