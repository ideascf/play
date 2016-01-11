#!/bin/python
from gevent import monkey
monkey.patch_all()

import gevent

from task import hello
from tools import decorator, runner

import logging, sys
decorator.profile_log.addHandler(
    logging.StreamHandler(sys.stdout)
)
decorator.profile_log.setLevel('INFO')

@decorator.qps()
# @runner.ProcessRunner(1, 4)
@runner.ThreadRunner(1, 4)
@runner.GeventRunner(1, 1000)
def main():
    if hello.delay('hello').get():
        return True
    else:
        return False

if __name__ == '__main__':
    main()
