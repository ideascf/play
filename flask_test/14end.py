from flask import Flask, g
import flask

class settings(object):
    DEBUG = True
    SERVER_IP = 'localhost'
    SERVER_PORT = '5000'
    TEMPLATE_FOLDER = None
    STATIC_FOLDER = None

class JINJA2_GLOBALS(object):
    pass

class JINJA2_FILTERS(object):
    pass

bp_test = flask.Blueprint('test')
bp_ball = flask.Blueprint('ball')


def create_app(debug=settings.DEBUG):
    app = Flask(
        __name__,
        template_folder=settings.TEMPLATE_FOLDER,
        static_folder=settings.STATIC_FOLDER,
    )

    # 注册所有的蓝图
    app.register_blueprint(bp_test)
    app.register_blueprint(bp_ball)

    # 配置jinja模板
    app.jinja_env.globals.update(JINJA2_GLOBALS)
    app.jinja_env.filters.update(JINJA2_FILTERS)

    # 配置secret_key
    app.secret_key = 'secret_key'


    @app.before_request
    def before_request():
        g.file = open('./nothing')

    @app.after_request
    def after_request(exception):
        g.file.close()


    return app