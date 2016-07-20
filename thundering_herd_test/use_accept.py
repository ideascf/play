# coding=utf-8
"""
$ python use_accept.py

<Process(Process-1, started)> is running
<Process(Process-2, started)> is running
<Process(Process-3, started)> is running
<Process(Process-4, started)> is running
<Process(Process-1, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50506)
<Process(Process-2, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50508)
<Process(Process-3, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50510)
<Process(Process-4, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50512)
<Process(Process-1, started)> <socket._socketobject object at 0x7fd0b9002590> ('127.0.0.1', 50514)
<Process(Process-2, started)> <socket._socketobject object at 0x7fd0b9002590> ('127.0.0.1', 50516)
<Process(Process-3, started)> <socket._socketobject object at 0x7fd0b9002590> ('127.0.0.1', 50518)
<Process(Process-4, started)> <socket._socketobject object at 0x7fd0b9002590> ('127.0.0.1', 50520)
<Process(Process-1, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50522)
<Process(Process-2, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50524)
<Process(Process-3, started)> <socket._socketobject object at 0x7fd0b9002520> ('127.0.0.1', 50526)

"""

import multiprocessing
import base

def worker(listener):
    cp = multiprocessing.current_process()
    print cp, 'is running'

    while True:
        sock, addr  = listener.accept()
        print cp, sock, addr


if __name__ == '__main__':
    base.bootstrap(worker)
