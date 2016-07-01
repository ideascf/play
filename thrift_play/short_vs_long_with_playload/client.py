# coding=utf-8
"""
1. 单进程、单线程
    - 短链接
      10.0045740604秒执行了 (short_ping) 13183次，成功13183次，失败0次。QPS是1317.6972773/s。
    - 长连接
      10.0046858788秒执行了 (long_ping) 50391次，成功50391次，失败0次。QPS是5036.73984478/s。
2. 单进程、多线程(10)
    - 短链接
      10.0551900864秒执行了 (short_ping) 18653次，成功18653次，失败0次。QPS是1855.06189737/s。
    - 长连接
      10.0131649971秒执行了 (long_ping) 51797次，成功51797次，失败0次。QPS是5172.88989196/s。
3. 单进程、单线程、多协程(10)
    - 短链接
      10.0227820873秒执行了 (short_ping) 12167次，成功12167次，失败0次。QPS是1213.93440404/s。
    - 长连接
      10.0158090591秒执行了 (long_ping) 43258次，成功43258次，失败0次。QPS是4318.97211145/s。
"""
from gevent import monkey
monkey.patch_all()

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import threading

from hello.Hello import Client
from tools import perf


def gen_short_client():
    """
    生成短链接的客户端
    :return:
    :rtype: Client
    """

    sock = TSocket.TSocket()
    transport = TTransport.TBufferedTransport(sock)
    proto = TBinaryProtocol.TBinaryProtocol(transport)

    transport.open()
    client = Client(proto)

    return client

l = threading.local()
def gen_long_client():
    """
    生成长连接的客户端
    :return:
    :rtype: Client
    """

    if not hasattr(l, 'long_client'):
        print('new client...')
        l.long_client = gen_short_client()

    return l.long_client

# @perf.qps()
# @perf.qps(concurrency=10, runner_name='thread')
@perf.qps(concurrency=10, runner_name='gevent')
def short_ping():
    cli = gen_short_client()
    cli.ping('ping')
    cli._iprot.trans.close()

    return True

# @perf.qps()
# @perf.qps(concurrency=10, runner_name='thread')
@perf.qps(concurrency=10, runner_name='gevent')
def long_ping():
    cli = gen_long_client()
    cli.ping('ping')

    return True

def main():
    perf.set_profile_log()


    short_ping()
    # long_ping()


if __name__ == '__main__':
    main()
