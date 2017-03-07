#!/usr/bin/env python
# coding=utf-8
use_gevent = False

if use_gevent:
    from gevent import monkey
    monkey.patch_all(thread=False)

from gevent.pywsgi import WSGIServer

from tornado.wsgi import WSGIApplication
import tornado.web
import tornado.wsgi
import tornado.ioloop
from tornado.gen import coroutine
from tornado.httpclient import AsyncHTTPClient

import requests


url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/mancard/js/config_8d7437e6.js'

class GeventHandler(tornado.web.RequestHandler):
    def get(self):
        requests.get(url)
        print '####'
        self.write('hello')


class TornadoHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self):
        c = AsyncHTTPClient()
        yield c.fetch(url)
        print '####'
        self.write('hello')

gevent_handlers = [
    (r'/', GeventHandler)
]

tornado_handlers = [
(r'/', TornadoHandler)
]


def run_gevent():
    application = WSGIApplication(gevent_handlers)
    server = WSGIServer(('', 9010), application)
    server.serve_forever()

def run_tornado():
    application = tornado.web.Application(tornado_handlers)
    application.listen(9010)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    if use_gevent:
        run_gevent()
    else:
        run_tornado()
