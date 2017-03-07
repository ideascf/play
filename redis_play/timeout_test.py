import redis
import gevent
import time
from gevent import timeout
from gevent import pool
r = redis.StrictRedis.from_url(url = 'redis://:password@127.0.0.1:4600', max_connections=30)
t = 3

def work():
    while True:
        try:
            with timeout.Timeout(3):
                st = time.time()

                r.expire('b', 1800)

                et = time.time()

                print 'cost: ', et-st
        except timeout.Timeout as e:
            print 'timeout', e
        except Exception as e:
            print e

        time.sleep(0.01)


def main():
    p = pool.Pool(20)
    while True:
        p.spawn(work)


if __name__ == '__main__':
    main()
