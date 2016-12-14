# coding=utf-8
from gevent import monkey
monkey.patch_all()

import GreenletProfiler
import time
import gevent



GreenletProfiler.set_clock_type('cpu')

cnt = 0
alive = True


def work():
    global cnt, alive

    while alive:
        cnt += 1
        gevent.sleep()

        # print gevent.getcurrent()


def work2():
    global cnt

    cnt += 1
    gevent.sleep()


def start():
    l = [
        gevent.spawn(work)
        for _ in range(1000)
    ]
    gevent.joinall(l)


def start2():
    global alive

    from gevent import pool
    p = pool.Pool(1000)

    while alive:
        p.spawn(work2)


def main():
    global alive

    st = time.time()
    try:
        GreenletProfiler.start()
        start()
    except KeyboardInterrupt:
        alive = False
    finally:
        GreenletProfiler.stop()

        et = time.time()

        print 'total time:', et - st
        print 'CNT:', cnt
        print 'QPS:', cnt / (et - st)
        print
        print

        stats = GreenletProfiler.get_func_stats()
        stats.print_all()
        stats.save('profile.callgrind', type='callgrind')



if __name__ == '__main__':
    main()
