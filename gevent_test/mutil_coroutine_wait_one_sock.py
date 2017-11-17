from gevent import monkey
monkey.patch_all()


import gevent
import socket
import threading

'''
Traceback (most recent call last):
  File "/Users/cf/anaconda/envs/py2/lib/python2.7/site-packages/gevent/greenlet.py", line 536, in run
    result = self._run(*self.args, **self.kwargs)
  File "/Users/cf/code/python/play/gevent_test/mutil_coroutine_wait_one_sock.py", line 12, in serve
    print threading.current_thread(), sock.recv(4)
  File "/Users/cf/anaconda/envs/py2/lib/python2.7/site-packages/gevent/_socket2.py", line 283, in recv
    self._wait(self._read_event)
  File "/Users/cf/anaconda/envs/py2/lib/python2.7/site-packages/gevent/_socket2.py", line 176, in _wait
    raise _socketcommon.ConcurrentObjectUseError('This socket is already used by another greenlet: %r' % (watcher.callback, ))
ConcurrentObjectUseError: This socket is already used by another greenlet: <bound method Waiter.switch of <gevent.hub.Waiter object at 0x10fb34af0>>
Wed Jun  7 10:04:16 2017 <Greenlet at 0x10fb327d0: serve(<socket at 0x10fb4b050 fileno=6 sock=127.0.0.1:999)> failed with ConcurrentObjectUseError
'''

def serve(sock):
    while True:
        print threading.current_thread(), sock.recv(4)


def main():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 9999))
    sock.listen(5)
    new_conn,_ = sock.accept()


    l = [
        gevent.spawn(serve, new_conn)
        for _ in range(2)
    ]
    while True:

        try:
            gevent.joinall(l)
        except KeyboardInterrupt :
            sock.close()
            return


if __name__ == '__main__':
    main()
