# coding=utf-8
from gevent import monkey
monkey.patch_all()

import gevent
from gevent import pool
import time

def worker(index=0, sleep_time=1):
    print (index, 'worker, before sleep')
    time.sleep(sleep_time)
    print (index, 'worker, after sleep')


def main():
    p = pool.Pool(2)

    start = time.time()
    index = 0
    while time.time() < start+2:
        p.spawn(worker, index)
        index += 1

    p.join()

# 测试pool：是因为pool满了，调用self._semaphore.acquire()才导致切到了hub的
def main_1():
    p = pool.Pool(3)
    create_full = True

    if create_full:
        while len(p) < p.size:
            p.spawn(worker, index=len(p), sleep_time=len(p))

        # 额外再创建一个，就会切到hub，导致之前创建的greenlet被调用。
        # 这次创建greenlet会失败，因为pool已经满了，要等待有空位让出才会创建
        # 即当有 之前创建的greenlet死亡时，才会切到这个greenlet来创建新的greenlet
        g = p.spawn(worker)

        # 创建完新的greenlet后，如果我们不回到hub，那么剩余的greenlet将得不到调度，且将直接退出进程
        # 所以要保证所有的greenlet均被执行，我们必须调用一些方法，去保证当还有greenlet没有执行完成时，能正确的回到hub
        # 比如 joinall(当有greenlet没有执行完成时，会再次调用waiter.get，这时会再次切到hub)；
        # 或 while True: pool.spawn() 不断的创建新的greenlet，直到pool满了，被动的切换到hub
        # 再或 hub.join： 它会等待所有已经创建的greenlet执行完成后退出
        print(len(p))
        p.join()  # wait所有的greenlet退出
    else:
        # 因为pool未满，不会切换到hub， 所以这里的worker不会被调用
        while len(p) < p.size - 1:  # 刻意不把pool创建满
            p.spawn(worker)  # 观察worker会不会被调用


if __name__ == '__main__':
    # main()
    main_1()
