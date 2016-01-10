from gevent import monkey
monkey.patch_all()
import gevent

import time


def gevent_sleep():
    print('hello....')
    gevent.sleep(1)
    print('world....')

def time_sleep():
    print('hello....')
    time.sleep(1)
    print('world....')




if __name__ == '__main__':
    # main()
    r1 = gevent.spawn(gevent_sleep)
    r2 = gevent.spawn(time_sleep)
    r4 = gevent.spawn(gevent_sleep)

    all_coroutine = [r1, r2, r4]
    all_coroutine.extend([
                gevent.spawn(gevent_sleep)
                for i in range(10)
            ])

    gevent.joinall(all_coroutine)
