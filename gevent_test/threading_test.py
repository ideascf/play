from gevent import monkey
monkey.patch_all()
# monkey.patch_thread(threading=False, _threading_local=False)
#
import threading
import time

g_local = monkey.get_original('thread', '_local')()
# g_local = threading.local()
g_local.a = 'haha'

def work(index):
    global g_local

    print threading.currentThread()
    print type(g_local)
    g_local.a = index
    time.sleep(index)

    print g_local.a

def start_thread(index):
    t = threading.Thread(target=work, args=(index,))
    t.start()

    return t


def main():
    threads = [
        start_thread(index)
        for index in range(3)
    ]

    map(
        lambda t: t.join(),
        threads
    )

if __name__ == '__main__':
    main()
