# coding=utf-8
from gevent import monkey
monkey.patch_all()

import gevent
import subprocess
import os
import sys
import time


def work(cnt, pwrite):
    print cnt, os.getpid(), os.getppid()

    with os.fdopen(pwrite, 'wb') as f:
        f.write('1')


def launcher(i):
    pread, pwrite = os.pipe()
    pid = os.fork()

    if pid == 0:  # child
        os.close(pread)
        time.sleep(2-i)
        work(i, pwrite)
        print 'child finish', os.getpid(), os.getppid()
        sys.exit(0)
    else:
        os.close(pwrite)
        with os.fdopen(pread, 'r') as f:
            f.read(1)

        print 'parent finish', os.getpid()


def main():
    # l = []
    # for i in range(2):
    #     print 'launcher new greenlet', os.getpid()
    #     g = gevent.spawn(launcher, i)
    #     l.append(g)


    # gevent.joinall(l)
    launcher(0)
    launcher(1)
    gevent.sleep(3)



if __name__ == '__main__':
    main()
