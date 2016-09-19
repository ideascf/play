# coding=utf-8
import pymysql
from pymysql.cursors import  Cursor
import multiprocessing
import subprocess
import gevent


def work(cursor):
    """

    :param cursor:
    :type cursor: Cursor
    :return:
    """

    for _ in range(100000):
        #cursor.execute('update xxx set foo=foo+1 where id = 3')
        cursor.execute('update xxx set foo=foo+1')


def main():
    con = pymysql.Connection(
        host='127.0.0.1',
        port=3306,
        user='qf',
        password='123456',
        database='test',
        autocommit=True,
    )

    cursor = con.cursor()

    g = [
        gevent.spawn(work, cursor)
        for _ in range(10)
    ]
    gevent.joinall(g)


if __name__ == '__main__':
    l = [
        multiprocessing.Process(target=main)
        for _ in range(10)
    ]
    map(lambda p: p.start(), l)
    map(lambda p: p.join(), l)
