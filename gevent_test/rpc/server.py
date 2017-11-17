# coding=utf-8
from gevent import monkey
monkey.patch_all()

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from gevent.server import StreamServer

from hello.Hello import Processor
from hello.Hello import Iface

tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

class HelloHandler(Iface):
    def ping(self, str):
        print 'ping...', len(str)
        return 'pong'

    def dozen(self):
        print 'dozen...'
        return ['pong', 'pong']

def handle(client_sock, client_addr):
    tsock = TSocket.TSocket(client_addr[0], client_addr[1])
    tsock.setHandle(client_sock)

    transport = tfactory.getTransport(tsock)
    protocol = pfactory.getProtocol(transport)
    processor = Processor(HelloHandler())


    try:
        while True:
            if not processor.process(protocol, protocol):
                break
    except TTransport.TTransportException as e:
        if e.type == TTransport.TTransportException.END_OF_FILE:
            print '!!!closed'
            pass
        else:
            raise


def create_tserver():
    sock = TSocket.TServerSocket()
    handler = HelloHandler()
    processor = Processor(handler)
    server = TServer.TThreadPoolServer(processor, sock, tfactory, pfactory)

    return server

def create_gserver():
    server = StreamServer(('127.0.0.1', 9090), handle=handle)

    return server

def main():
    server = create_gserver()
    server.serve_forever()

    # server = create_tserver()
    # server.serve()

if __name__ == '__main__':
    main()
