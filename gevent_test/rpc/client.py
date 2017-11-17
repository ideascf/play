# coding=utf-8
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hello.Hello import Client

def gen_client():
    sock = TSocket.TSocket()
    transport = TTransport.TBufferedTransport(sock)
    proto = TBinaryProtocol.TBinaryProtocol(transport)

    transport.open()
    client = Client(proto)

    return client

def main():
    client = gen_client()

    print client.ping('ping'*1024*1024)
    print client.ping('ping')
    print client.ping('ping')
    print client.ping('ping')
    print client.dozen()


if __name__ == '__main__':
    main()
