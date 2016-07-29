# coding=utf-8
from werkzeug.wrappers import Request, Response


def application1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])

    return ['Hello World']


def application2(environ, start_response):
    response = Response('Hello World', mimetype='text/plain')

    return response(environ, start_response)


def application3(environ, start_response):
    request = Request(environ)
    text = 'Hello {}'.format(request.args.get('name', 'World'))

    response = Response(text, mimetype='text/plain')

    return response(environ, start_response)