from flask import Flask
from flask import session
from datetime import timedelta

app = Flask(__name__)


app.secret_key = 'abvlJYOJ@$%*"<~@'  # 用来加密cookie的？？

session['key'] = 1
session.pop('logged_in', None)

session.clear()


session.permanent = True  # 是否持久化session
app.permanent_session_lifetime = timedelta(minutes=5)  # 生命周期