import gevent

from tools import decorator

def foo():
    pass

@decorator.timeit
def main():
    [
        gevent.spawn(foo)
        for _ in range(1000 * 100)
    ]

if __name__ == '__main__':
    main()
