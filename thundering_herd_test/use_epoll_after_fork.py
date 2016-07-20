# coding=utf-8
"""
$ python use_epoll_after_fork.py
<Process(Process-1, started)> is running
<Process(Process-2, started)> is running
<Process(Process-3, started)> is running
<Process(Process-4, started)> is running
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46234)
<Process(Process-1, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46236)
<Process(Process-2, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46238)
<Process(Process-1, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46240)
<Process(Process-3, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46242)
<Process(Process-1, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46244)
<Process(Process-2, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46246)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46248)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46250)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46252)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46254)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46256)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46258)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46260)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46262)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46264)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46266)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46268)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46270)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46272)
<Process(Process-3, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46274)
<Process(Process-2, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46276)
<Process(Process-1, started)> <socket._socketobject object at 0x2b4c410881a0> ('192.168.0.152', 46278)
<Process(Process-4, started)> <socket._socketobject object at 0x2b4c41088130> ('192.168.0.152', 46280)

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

def worker(listener):
    """

    :param listener:
    :type listener: socket._socketobject
    :return:
    """

    cp = multiprocessing.current_process()
    print cp, 'is running'

    poller = select.epoll()
    poller.register(listener.fileno(), READ | ERROR)

    while True:
        event_pairs = poller.poll()
        for each in event_pairs:
            fd, events = each
            if READ | events:
                sock, addr = listener.accept()
                print cp, sock, addr
            else:
                print cp, 'wakeup do NOTHING', events


if __name__ == '__main__':
    base.bootstrap(worker)