from flask import Flask

app = Flask(__name__)

"""
    配置文件加载或更新大致可以分为：
        1. 直接把app.config当做字典来更新
        2. 调用app.from_object，从class、object、module中加载
        3. 调用app.from_envvar，从环境变量指定的文件中加载
        4. 调用app.from_pyfile，从py文件中加载
"""

# 方案1，把config当做一个dict来更新
app.config.update(
    {
        'DATABASE': '/tmp/flaskr.db',
        'DEBUG': True,
        'SECRET_KEY': 'development_key',
        'USERNAME': 'admin',
        'PASSWORD': 'admin',
    }
)
app.config['HOST'] = 'www.xxx.com'

# 方案2, 从环境变量指定的文件中加载配置
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# 方案3， 从module中加载
DATABASE = '/tmp/flaskr.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development_key'

app = Flask(__name__)
app.config.from_object(__name__)

# 方案4， 从obj中加载
class Config(object):
    DEBUG = True
    TESTING = True
    DATABAS = '/tmp/flaskr.db'

class ArticleConfig(Config):
    USERNAME = 'admin'
    PASSWORD = 'admin'

app.config.from_object(ArticleConfig)

# 方案5，从文件中加载
app.config.from_pyfile('config.py')