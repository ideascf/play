# coding=utf-8
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from hello.Hello import Processor
from hello.Hello import Iface

class HelloHandler(Iface):
    def ping(self, str):
        return 'pong'

    def dozen(self):
        return ['pong', 'pong']


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
