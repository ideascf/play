# coding=utf-8
import json
import sys


def main():
    d = json.loads(sys.argv[1])
    print 'hello', type(d), d, sys.argv[2]


if __name__ == '__main__':
    main()