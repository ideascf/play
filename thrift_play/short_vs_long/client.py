# coding=utf-8
"""
# 结果
以下测试，在服务端有0.5秒的业务逻辑耗时下得出：
1. 单进程、单线程
    - 短链接
      10.0347189903秒执行了 (short_ping) 20次，成功20次，失败0次。QPS是1.99308022669/s。
    - 长连接
      10.0233681202秒执行了 (long_ping) 20次，成功20次，失败0次。QPS是1.99533727188/s。
2. 单进程、多线程(10)
    - 短链接
      10.0624928474秒执行了 (short_ping) 200次，成功200次，失败0次。QPS是19.8757905255/s。
    - 长连接
      10.0366990566秒执行了 (long_ping) 200次，成功200次，失败0次。QPS是19.926870266/s。
3. 单进程、单线程、多协程(10)
    - 短链接
      10.1149840355秒执行了 (short_ping) 200次，成功200次，失败0次。QPS是19.7726461355/s。
    - 长连接
      10.0474460125秒执行了 (long_ping) 200次，成功200次，失败0次。QPS是19.9055560738/s。

# 总结
- 当业务逻辑耗时:连接建立耗时，比例很高的时候，且*并发数不高*的时候，长短连接差异性不是很明显
- 但本测试没有将服务端压倒极限，以看短链接和长连接的差异(差异性主要在于不断的连接建立和断开引起的性能开销)
- 故，本测试*不具有*代表性意义
"""


# from gevent import monkey
# monkey.patch_all()

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
@perf.qps(concurrency=10, runner_name='thread')
# @perf.qps(concurrency=10, runner_name='gevent')
def short_ping():
    cli = gen_short_client()
    cli.ping('ping')
    cli._iprot.trans.close()

    return True

# @perf.qps()
@perf.qps(concurrency=10, runner_name='thread')
# @perf.qps(concurrency=10, runner_name='gevent')
def long_ping():
    cli = gen_long_client()
    cli.ping('ping')

    return True

def main():
    perf.set_profile_log()


    # short_ping()
    long_ping()


if __name__ == '__main__':
    main()
