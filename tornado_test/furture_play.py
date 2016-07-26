# coding=utf-8
from __future__ import print_function

from tornado import ioloop
from tornado.process import Subprocess
from tornado.gen import coroutine


def finish_callback(future):
    print('sleep finished')
    print('furture, done: ', future.done())
    print('furture, result: ', future.result())


def dumy_callback():
    print('dumy callbacked')


def work1():
    p = Subprocess(['sleep', '5'])
    future = p.wait_for_exit()

    ioloop.IOLoop.instance().add_future(future, finish_callback)
    print('work1: After add_future....')

    ioloop.IOLoop.instance().add_callback(dumy_callback)
    print ('work1: After add_callback...')


@coroutine
def work2():
    p = Subprocess(['sleep', '2'])
    print('work2: Before yield')
    ret = yield p.wait_for_exit()
    print('work2: After yield, result:', ret)


def main():
    loop = ioloop.IOLoop.instance()
    loop.add_callback(work1)
    loop.add_callback(work2)

    loop.start()


if __name__ == '__main__':
    main()
