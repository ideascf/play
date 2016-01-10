from flask import Flask
import flask

app = Flask(__name__)


@app.route('/foo')
def foo():
    # return flask.redirect('/')

    # url_for  用来获得一个函数(被flask称为endpoint)的url
    return flask.redirect(flask.url_for('main'))


@app.route('/')
def main():
    return 'hello 11redirect'


if __name__ == '__main__':
    app.run(debug=True)
