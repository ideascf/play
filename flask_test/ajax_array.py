# coding=utf-8
import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    with open('./index.html') as f:
        return f.read()

@app.route('/p', methods=['get', 'post'])
def p():
    print 'args', request.args
    print 'form', request.form

    return ''


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()