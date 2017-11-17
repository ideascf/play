# coding=utf-8
import flask
from flask import request

app = flask.Flask(__name__)

@app.errorhandler(404)
def error(*args, **kwargs):
    print 'args', request.args
    print 'form', request.form
    print 'cookie', request.cookies

    return 'hello'

@app.route('/', methods=['get', 'post'])
def index():
    with open('./index.html') as f:
        return f.read()



@app.route('/p', methods=['get', 'post'])
def p():
    print 'args', request.args
    print 'form', request.form
    print 'cookie', request.cookies

    return 'hello'


def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
