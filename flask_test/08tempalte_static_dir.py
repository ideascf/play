from flask import Flask

# 定义app使用的template和static目录
app = Flask(__name__, template_folder='./template', static_folder='.')

@app.route('/', methods=['GET'])
def send_file():  # 函数名不能为static
    print('send_file')

    # 1. 当找不到文件时，会返回404
    # 2. 会根据flask app 配置的static_folder来找文件
    return app.send_static_file('./nothing')


if __name__ == '__main__':
    app.run()
