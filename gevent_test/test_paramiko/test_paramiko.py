import traceback

from gevent import monkey
monkey.patch_all()

import random
import csv
import gevent
import paramiko
from gevent import pool
import threading

from client_pool import BlockingClientPool, get_client
from sftp_conn import SFTPConn

host = '192.168.0.7'
port = '22'
username = 'mysftp'
password = '123456'
remote_path = '/download/smartpay/settlements/'
filename = '2088221981261204_settlement_20160923.txt'

client_pool = BlockingClientPool(
    SFTPConn,
    2,
    host=host,
    port=port,
    username=username,
    password=password,
)


def work():
    reader = None

    while True:
        try:
            with get_client(client_pool) as c:
                reader = c.do(filename, max_retry=3, delimiter='|')
        except Exception as e:
            print e
            print traceback.format_exc()

        print threading.currentThread(), reader, next(reader)
        gevent.sleep(random.random())
    # f.close()

def main():
    # work()
    # return
    p = pool.Pool(200)

    while True:
        p.spawn(work)

    # p.join()


if __name__ == '__main__':
    main()