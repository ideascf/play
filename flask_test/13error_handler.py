from flask import Flask
import flask


app = Flask(__name__)

"""
    @ATTENTION 属性的名字是errorhandler,不是error_handlers。前者是方法，后者是变量
"""


# 当发生404错误时，会调用这个handler
@app.errorhandler(404)
def not_found_error(error):
    return 'in my not_found_error_handler: %s' % error


# 当服务器发生内部错误时，会调用这个handler
@app.errorhandler(500)
def internal_error(error):
    return 'in my internal_error_handler: %s' % error


@app.route('/error')
def gen_err():
    return 1/0


if __name__ == '__main__':
    app.run(debug=True)
