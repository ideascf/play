# coding=utf-8
from gevent import monkey
monkey.patch_all()

import gevent
import subprocess
import multiprocessing
from threading import Thread


print Thread, dir(Thread.__module__)



def work(a):
    print a, 'hello', multiprocessing.current_process()

def main():
    p = multiprocessing.Pool(processes=2)
    print 'create processing OK'

    # for i in range(20):
    #     p.apply_async(work, args=(i,))

    p.close()
    p.join()

if __name__ == '__main__':
    # pass
    main()
