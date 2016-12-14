# coding=utf-8
import greenlet

import time

g1 = g2 = None
cnt = 0
alive = True

def work1():
    global alive, cnt

    while alive:
        cnt += 1
        g2.switch()


def work2():
    global alive, cnt

    while alive:
        cnt += 1
        g1.switch()



def start():
    global g1, g2

    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)

    g1.switch()

def main():
    global alive


    st = time.time()
    try:
        start()
    except KeyboardInterrupt:
        alive = False
    finally:
        et = time.time()
        print 'total time:', et - st
        print 'CNT:', cnt
        print 'QPS:', cnt/(et-st)


if __name__ == '__main__':
    main()