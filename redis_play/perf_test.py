# coding=utf-8
import json
import time
from gevent import monkey
monkey.patch_all()

import gevent
from gevent import pool
import redis


url = 'redis://192.168.0.9:46379/0'
r = redis.StrictRedis(
    connection_pool=redis.ConnectionPool.from_url(url),
)

cnt = 0
data = 'a'*256
playload = {
    'msg_id': '1f806994-c8af-490d-8516-43aa5abae8c8',
    'msg_type': 1,
    'platform': 'android',
    'sdk': 'qfpay',
    'apptype': 401,
    'userid': 123456,
    'deiceid': '1f806994-c8af-490d-8516-43aa5abae8c8',

    'body': data,
}
playload_str = json.dumps(playload)
rpush_times = 6
dumps_times = 3
loads_times = 3

def work():
    global cnt

    while True:
        cnt += 1

        for _ in range(dumps_times):
            json.dumps(playload)
        for _ in range(loads_times):
            json.loads(playload_str)

        for _ in range(rpush_times):
            r.rpush('b', playload_str)




def main():
    st = time.time()
    try:
        p = pool.Pool(1024)

        while True:
            p.spawn(work)
            st = time.time()

    except KeyboardInterrupt:
        pass
    finally:
        et = time.time()
        print 'time:', et - st
        print 'REQ:', cnt
        print 'QPS:', cnt/(et-st)

if __name__ == '__main__':
    main()

