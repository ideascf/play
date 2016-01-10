from flask import Flask
from flask import Response, jsonify, json

app = Flask(__name__, static_folder='.')


# WRONG WAY, shouldn't use tuple but list
# @app.route('/', methods=('GET', 'POST'))

@app.route('/', methods=['GET', 'POST'])
def main():
    return 'hello world'


@app.route('/wrong', methods=('POST'))
def wrong_methods():
    return 'in wrong methods'


@app.route('/post', methods=['post'])
def post():
    return 'in post'


@app.route('/static', methods=['GET'])
def send_file():  # 函数名不能为static
    print('send_file')

    # 1. 当找不到文件时，会返回404
    # 2. 会根据flask app 配置的static_folder来找文件
    return app.send_static_file('./nothing')


@app.route('/json')
def json_ret():
    # 相当于json.dumps(dict(ok=True, data={'a': 1}))
    return jsonify(ok=True, data={'a': 1})


@app.route('/response')
def response():
    # 用来构造响应报文
    return Response(
        '{"a": 1}ss',
        mimetype='text/javascript'
    )


if __name__ == '__main__':
    app.run(debug=True)
