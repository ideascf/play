# coding=utf-8
from __future__ import print_function

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from test.Test import Client

def gen_client():
    sock = TSocket.TSocket()
    transport = TTransport.TBufferedTransport(sock)
    proto = TBinaryProtocol.TBinaryProtocol(transport)

    transport.open()
    client = Client(proto)

    return client

def main():
    client = gen_client()

    print(client.hello(None))  # use default value 99999
    print(client.hello(123))
    print(client.hello('hello'))  # raise struct.error: cannot convert argument to integer


if __name__ == '__main__':
    main()
