import gevent

def foo():
    print 'foo...'

def bar():
    print 'bar...'

def main():
    gevent.spawn(foo)
    g = gevent.spawn(bar)

    g.join()

if __name__ == '__main__':
    main()

