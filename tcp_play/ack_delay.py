import socket
import sys
import time
import logging


ADDR = ('0.0.0.0', 39999)

log = logging.getLogger()
hdlr = logging.StreamHandler(sys.stdout)
log.addHandler(hdlr)
log.setLevel('DEBUG')

def now():
    return int(time.time()*1000)


def client():
    sock = socket.socket()
    sock.connect(ADDR)
    sock.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, 0)

    while True:
        start = now()
        sock.sendall('ping')
        log.info('client, send1: %s', now())

        sock.sendall('ping')
        log.info( 'client, send2: %s', now())

        sock.recv(4)
        log.info('client, recv: %s', now())

        end = now()
        log.info('client, cost: %s ms', end-start)  # should print 40ms

        log.info('')
        log.info('')

        time.sleep(1)

def serve_one(sock):
    sock.setsockopt(socket.SOL_SOCKET, socket.TCP_QUICKACK, 0)

    while True:
        ret = sock.recv(4)
        if ret == '':
            return
        log.info( 'server, recv1: %s', now())

        ret = sock.recv(4)
        if ret == '':
            return
        log.info( 'server, recv2: %s', now())

        sock.sendall('pong')
        log.info('server, send: %s', now())

        log.info('')
        log.info('')




def server():
    s = socket.socket()
    s.bind(ADDR)
    s.listen(10)
    sock,addr = s.accept()
    serve_one(sock)

def main():
    entry = sys.argv[1]
    if entry == 's':
        server()
    else:
        client()

if __name__ == '__main__':
    main()

