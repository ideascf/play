from gevent import monkey
monkey.patch_all()

import gevent
import pymysql


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, database='test', user='test', password='test')
    print(conn.get_server_info())
    ret = conn.query("INSERT INTO `count` (`text`) VALUES ('{0}')".format('haha'))
    print(ret)

if __name__ == '__main__':
    gevent.joinall(
        [
            gevent.spawn(main)
            for i in range(10)
        ]
    )
