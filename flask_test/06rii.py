from flask import Flask
from flask import g

app = Flask(__name__)

"""
1. 在request开始和结束，做一些事情
2. app 和 blueprint都有
    1. blueprint的hook
        1. before_request 和 after_request 和 teardown_request:
            a. 给指定蓝图注册hook，仅对该蓝图生效
        2. before_app_request、after_app_request、teardown_app_request：
            a. 给app注册hook，对该app所有request生效
    2. app的hook
        1. before_request 和 after_request 和 teardown_request

    3. 顺序：
        before_app_request -> before_request -> after_request -> after_app_request
        -> teardown_app_request -> teardown_request
"""

#  call the function, when the APP's first request
@app.before_first_request
def before_first_request():
    print('app.before_first_request')


# call the function, before one request start
@app.before_request
def before_request():
    print('app.before_request')
    g.file = open('./nothing', 'w')

# call the function, after one reques is finished.
# 传入已经生成的response对象，也必须返回一个response对象
@app.after_request
def after_request(response):
    print('app.after_request', response)

    return response

# call the function, after one request finished
@app.teardown_request
def teardown_request(exception):  # yes，HAVE an argument
    print('app.teardown_request')
    g.file.close()




@app.route('/')
def main():
    info = 'before_request_funcs: {}, after_request_funcs: {}'.format(
        app.before_request_funcs,  # the request's BEFORE call.
        app.after_request_funcs  # the request's AFTER call. uch, now is empty.
    )

    return 'hello 06rii'+info

if __name__ == '__main__':
    app.run(debug=True)
