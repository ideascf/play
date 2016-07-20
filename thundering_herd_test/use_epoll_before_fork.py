# coding=utf-8
"""
$ python use_epoll_before_fork.py


"""

import socket
import multiprocessing
import select
import base


_EPOLLIN = 0x001
_EPOLLPRI = 0x002
_EPOLLOUT = 0x004
_EPOLLERR = 0x008
_EPOLLHUP = 0x010
_EPOLLRDHUP = 0x2000
_EPOLLONESHOT = (1 << 30)
_EPOLLET = (1 << 31)

# Our events map exactly to the epoll events
NONE = 0
READ = _EPOLLIN
WRITE = _EPOLLOUT
ERROR = _EPOLLERR | _EPOLLHUP

def worker(pair):
    """

    :param listener:
    :type listener: (socket._socketobject, select.epoll)
    :return:
    """

    cp = multiprocessing.current_process()
    print cp, 'is running'
    listener, poller = pair


    while True:
        event_pairs = poller.poll()
        for each in event_pairs:
            fd, events = each
            if READ | events:
                sock, addr = listener.accept()
                print cp, sock, addr
            else:
                print cp, 'wakeup do NOTHING', events

def create_epoll(listener):
    poller = select.epoll()
    poller.register(listener.fileno(), READ | ERROR)

    return listener, poller


if __name__ == '__main__':
    base.bootstrap(worker, before_fork_callback=create_epoll)