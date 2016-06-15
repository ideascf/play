# -*- encoding=utf8
import gevent

def foo():
    print 'foo'

    # 错误， 将导致greenlet cycle
    # gevent.getcurrent().parent = gevent.greenlet.greenlet()

def main():
    g = gevent.Greenlet(foo)
    #  错误，将导致g不能启动，因为start会调用： self.parent.loop.run_callback(self.switch)
    # g.parent = gevent.greenlet.greenlet()

    g.start()
    # gevent.get_hub().loop.run()
    g.join()
    print 'after run'


if __name__ == '__main__':
    main()
