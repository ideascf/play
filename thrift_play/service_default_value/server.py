# coding=utf-8
from __future__ import print_function

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from test.Test import Processor
from test.Test import Iface

class HelloHandler(Iface):
    def hello(self, s):
        print(s)


def create_server():
    sock = TSocket.TServerSocket()

    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    handler = HelloHandler()
    processor = Processor(handler)
    server = TServer.TThreadPoolServer(processor, sock, tfactory, pfactory)

    return server

def main():
    server = create_server()
    server.serve()

if __name__ == '__main__':
    main()
