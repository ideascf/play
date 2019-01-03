from __future__ import print_function

import time
from gevent import monkey
monkey.patch_all()

import gevent
import socket
from gevent import server
import hashlib
import base64

def handler(sock, addr):
    """

    :param sock:
    :type sock: socket.socket
    :param addr:
    :type addr:
    :return:
    :rtype:
    """

    buf = sock.recv(1024)
    while buf:
        print(addr, time.time())
        print('recv: ', buf)
        key = ''
        for line in buf.split('\r\n'):
            if line.startswith('Sec-WebSocket-Key: '):
                key = line.split(' ')[1].strip('\r\n')
                break
        if key == '':
            sock.close()
            return

        s = hashlib.sha1()
        s.update(key)
        s.update("258EAFA5-E914-47DA-95CA-C5AB0DC85B11")
        ret = '''HTTP/1.1 101 Switching Protocols\r\nServer: nginx/1.6.2\r\nDate: Thu, 08 Jun 2017 15:01:46 GMT\r\nConnection: upgrade\r\nUpgrade: websocket\r\nSec-WebSocket-Accept: '''
        ret += base64.b64encode(s.digest())
        ret += '\r\n\r\n'
        print('ret: ', ret)
        sock.send(ret)

        while True:
            buf = sock.recv(1024)
            if len(buf) <= 0:
                print('close', time.time())
                sock.close()
                return
            print(buf)


def main(port=8001):

    s = server.StreamServer(('0.0.0.0', port), handler)
    s.start()
    s.serve_forever()

if __name__ == '__main__':
    main()
