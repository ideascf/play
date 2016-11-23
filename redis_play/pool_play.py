# coding=utf-8
from gevent import monkey
monkey.patch_all()

import gevent
from gevent import pool
import redis
url = 'redis://192.168.0.7:31004/0'

redis_pool = redis.ConnectionPool.from_url(url)


def work():
    while True:
        r = redis.StrictRedis(
            connection_pool=redis_pool
        )
        r.ping()
        print len(redis_pool._in_use_connections)


def main():
    p = pool.Pool(10000)

    i = 0
    while True:
        p.spawn(work)

        i += 1
        print i


if __name__ == '__main__':
    main()
