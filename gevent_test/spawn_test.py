import gevent

from tools import perf


def foo():
    pass

@perf.timeit
def main():
    [
        gevent.spawn(foo)
        for _ in range(1000 * 100)
    ]

if __name__ == '__main__':
    main()
