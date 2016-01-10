from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'Post'])
def main():
    args = request.args if request.method == 'GET' else request.form
    print(args)
    print(args.get('a', 'default'))

    return str(args)
    # return args  # ERROR! must return str


@app.route('/json', methods=['POST'])
def get_json():
    # if HEAD contain 'Content-Type: application/json'
    # such as: curl -d '{"a": 1}' -H 'Content-Type: application/json'
    data = request.get_json()

    return 'hello 04 %s' % str(data)


@app.route('/file', methods=['POST'])
def get_file():
    """
    <form action="/image/upload/" method="post" enctype="multipart/form-data">
    <input type="file" name="upload" />
    """

    # 获得上传的文件
    file = request.files.get('upload')

    return 'OK'


@app.route('/header')
def get_header():
    print(type(request.headers), request.headers)

    return str(request.headers)


if __name__ == '__main__':
    app.run(debug=True)
