#!/bin/python
from task import hello
from tools import decorator

import logging, sys
decorator.profile_log.addHandler(
    logging.StreamHandler(sys.stdout)
)
decorator.profile_log.setLevel('INFO')


def do():
    if hello.delay('hello').get():
        return True
    else:
        return False

@decorator.qps()
def main():
    return do()


@decorator.qps()
def main_0():
    return do()


def dummy():
    for _ in range(10000):
        a = 1 + 1


@decorator.qps()
def empty():
    dummy()

    return True

if __name__ == '__main__':
    # main()
    main_0()

    # empty()

    pass
