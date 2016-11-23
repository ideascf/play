from __future__ import print_function
from gevent import monkey
monkey.patch_all()

import gevent
import socket
from gevent import server

def handler(sock, addr):
    """

    :param sock:
    :type sock: socket.socket
    :param addr:
    :type addr:
    :return:
    :rtype:
    """
    print(addr)

    buf = sock.recv(1024)
    while buf:
        print('recv: ', buf)
        sock.send('pong')
        buf = sock.recv(1024)

def main(port=11111):

    s = server.StreamServer(('0.0.0.0', port), handler)
    s.start()
    s.serve_forever()

if __name__ == '__main__':
    main()