# coding=utf-8
from gevent import monkey
monkey.patch_all()

import json
import time
import logging
import gevent
from gevent import pool
import redis

# 全局工具
log = logging.getLogger()
hdlr = logging.FileHandler('./t.log')
log.addHandler(hdlr)
log.setLevel('DEBUG')

url = 'redis://192.168.0.9:46379/0'
r = redis.StrictRedis(
    connection_pool=redis.ConnectionPool.from_url(url),
)

# 统计变量
cnt = 0
alive = True
dumps_time = 0
loads_time = 0
rpush_time = 0
log_time = 0

# 测试参数
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
log_times = 0
pool_size = 5

def work():
    global cnt, dumps_time, loads_time, rpush_time, log_time
    global alive

    while alive:
        cnt += 1

        t1 = time.time()
        for _ in range(dumps_times):
            json.dumps(playload)
        t2 = time.time()
        dumps_time += (t2 - t1)


        for _ in range(loads_times):
            json.loads(playload_str)
        t3 = time.time()
        loads_time += (t3 - t2)


        for _ in range(rpush_times):
            r.rpush('b', playload_str)
        t4 = time.time()
        rpush_time += (t4 - t3)


        for _ in range(log_times):
            log.info(playload_str)
        t5 = time.time()
        log_time += (t5 - t4)


def stop(p):
    global alive

    from gevent import timeout
    to = timeout.Timeout(10)
    to.start()

    try:
        p.join()
    except gevent.Timeout:
        alive = False


def start():
    p = pool.Pool(pool_size)
    gevent.spawn(stop, p)

    while alive:
        st = time.time()
        p.spawn(work)

def main():
    global alive


    st = time.time()
    try:
        start()
        # work()
    except KeyboardInterrupt:
        alive = False
    finally:
        et = time.time()
        print 'total time:', et - st
        print 'CNT:', cnt
        print 'QPS:', cnt/(et-st)
        print
        print '\tdumps_time: ', dumps_time
        print '\tloads_time: ', loads_time
        print '\trpush_time: ', rpush_time
        print '\tlog_time: ', log_time

if __name__ == '__main__':
    main()

