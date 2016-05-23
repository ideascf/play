from gevent import monkey
monkey.patch_all()

import sys
import logging
import urllib2
import urllib
import gevent

log = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter('%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s')
handler.setFormatter(fmt)
log.addHandler(handler)
log.setLevel('DEBUG')

def do_request():
    log.info('before...')

    openner = urllib.URLopener()
    resp_str = openner.open('http://www.baidu.com')
    log.info('middle...')
    resp_str = openner.open('http://www.baidu.com')

    log.info('after...')

def main():
    all_evenlet = [
        gevent.spawn(do_request)
        for i in range(10)
    ]

    gevent.joinall(all_evenlet)


if __name__ == '__main__':
    main()
