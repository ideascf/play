from flask import Flask
from flask import Blueprint
import flask

"""
蓝图， 用来定义一系列具有统一前缀的URL的路由表。 这样可以更好的模块化。
你可以在每个模块中创建一个blueprint，然后main.py中app.register_blueprint注册这些blueprint。
比如： 给/article和/picture分别定义blueprint，这样就可以很好的组织URL路由表。

1. errorhandler: 可以为指定的蓝图定义专有的errorhandler
    a. 404错误，除非时蓝图内部函数触发的(如：flask.abort(404))，否则不会调用到蓝图的errorhandler
    b. 500错误，一直会调用app中的errorhandler

2. before_request 和 after_request 和 teardown_request:
    a. 给指定蓝图注册hook，仅对该蓝图生效
3. before_app_request、after_app_request、teardown_app_request：
    a. 给app注册hook，对该app所有request生效
4. 顺序：
    before_app_request -> before_request -> after_request -> after_app_request
    -> teardown_app_request -> teardown_request
"""

app = Flask(__name__)
bp_test = Blueprint('test', __name__, url_prefix='/test')
bp_foo = Blueprint('foo', __name__, url_prefix='/foo')

# 这是test蓝图的URL集
# /test/hello
@bp_test.route('/hello')
def test_hello():
    return 'test_hello'


# /test/world
@bp_test.route('/world')
def test_world():
    return 'test_world'


###### bp_test 的errorhandler测试
# /test/gen404  调用这个函数可以触发下面的test_not_found_handler函数
@bp_test.route('/gen404')
def gen_404():
    flask.abort(404)


# /test/gen500
@bp_test.route('/gen500')
def gen_500():
    flask.abort(500)

# bp_test的errorhandler，和其它蓝图errorhandler时独立的
"""
    Registers an error handler that becomes active for this blueprint
    only.
    1. Please be aware that routing does not happen local to a
    blueprint so an error handler for 404 usually is not handled by
    a blueprint unless it is caused inside a view function.
    2.Another special case is the 500 internal server error which is always looked
    up from the application.
"""
@bp_test.errorhandler(404)
def test_not_found_handler(error):
    return 'blue_print<bp_test>: in test_not_found_handler'

###### 测试request的hook函数
@bp_test.before_request
def test_before_request():
    print('bp_test: before_request')

@bp_test.after_request
def test_after_request(response):
    print('bp_test: after_request', response)

    return response

@bp_test.teardown_request
def test_teardown_request(exception):
    print('bp_test: teardown_request')

###### 测试request的hook函数，注册到app，而不是blueprint
@bp_test.before_app_request
def test_before_app_request():
    print('bp_test: before_app_request')

@bp_test.after_app_request
def test_after_app_request(response):
    print('bp_test: after_app_request', response)

    return response

@bp_test.teardown_app_request
def test_teardown_app_request(exception):
    print('bp_test: teardown_app_request', exception)



######## 这是foo蓝图的URL集
# /foo/football
@bp_foo.route('/football')
def foo_football():
    return 'foo_football'


# /foo/basketball
@bp_foo.route('/basketball')
def foo_basketball():
    return 'foo_basketball'


if __name__ == '__main__':
    app.register_blueprint(bp_foo)
    app.register_blueprint(bp_test)

    app.run(debug=True)
