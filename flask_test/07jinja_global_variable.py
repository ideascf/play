from flask import Flask
import jinja2

app = Flask(__name__)

JINJA2_GLOBALS = {'MY_PREFIX': 'chenfei'}
app.jinja_env.globals.update(JINJA2_GLOBALS)  # 注册jinja2模板中使用的全局变量

