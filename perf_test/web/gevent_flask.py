from gevent.wsgi import WSGIServer
from pure_flask import app

http_server = WSGIServer(('', 8888), app)
http_server.serve_forever()
