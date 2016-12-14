# coding=utf-8
import logging
import time

import sys

from tools import perf

perf.profile_log.addHandler(
    logging.StreamHandler(sys.stdout)
)
perf.profile_log.setLevel('INFO')

@perf.timeit
def main():
    for _ in xrange(1000 * 1000):
        time.time()


if __name__ == '__main__':
    main()