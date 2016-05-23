import urllib2

from tools import perf

TEST_URL = 'http://192.168.0.152:8888'
TEST_DATA = 'hello world'

@perf.qps()
def main():
    try:
        urllib2.urlopen(TEST_URL, TEST_DATA).read()
    except:
        return False
    else:
        return True

if __name__ == '__main__':
    main()
