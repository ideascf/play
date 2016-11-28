# coding=utf-8
import time
from gevent import monkey
monkey.patch_all()

import gevent

cnt = 0

def work():
    global cnt
    while True:
        cnt += 1
        gevent.sleep()

        # print gevent.getcurrent()

def main():

    try:
        l = [
            gevent.spawn(work)
            for _ in range(100)
        ]
        st = time.time()
        gevent.joinall(l)
    except KeyboardInterrupt:
        et = time.time()
        print cnt
        print et-st


if __name__ == '__main__':
    main()