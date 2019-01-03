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

def main(host='127.0.0.1', port=11111):

    sock = socket.socket()
    sock.connect((host,port))
    f = sock.makefile()

    d = 'abcd'*1024*10
    f.write(d)
    f.flush()

    read_len = 0
    while read_len < len(d):
        buf = f.read(1024)
        read_len += len(buf)
        print('now, read_len:', read_len)


if __name__ == '__main__':
    main()