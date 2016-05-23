#!/bin/python
from task import hello
from tools import perf

perf.set_profile_log()

def do():
    #if hello.delay('hello').get():
    if hello.delay('hello'):
        return True
    else:
        return False

@perf.qps()
def main():
    return do()


@perf.qps()
def main_0():
    return do()


def dummy():
    for _ in range(10000):
        a = 1 + 1


@perf.qps()
def empty():
    dummy()

    return True

if __name__ == '__main__':
    # main()
    main_0()

    # empty()

    pass
