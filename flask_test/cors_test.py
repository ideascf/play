# coding=utf-8
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/', methods=['GET', "HEAD", 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'])
def main():
    print request.headers
    print request.method
    print request.cookies

    response = Response()
    response.set_data('HELLO WORLD')

    # 设置允许的第三方网站的domain, 否则浏览器不会讲结果交付给第三方网站
    # 1. No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://www.example.com' is therefore not allowed access
    # 2. The 'Access-Control-Allow-Origin' header contains the invalid value 'null'. Origin 'http://www.example.com' is therefore not allowed access.
    response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    #response.headers['Access-Control-Allow-Origin'] = 'null'

    # 如果请求中的credientials为true，那么这个标志必须设置为true， 否则浏览器不会将结果交付给第三方网站
    # XMLHttpRequest cannot load http://localhost:5000/. Credentials flag is 'true', but the 'Access-Control-Allow-Credentials' header is ''.
    # It must be 'true' to allow credentials. Origin 'http://www.example.com' is therefore not allowed access.
    response.headers['Access-Control-Allow-Credentials'] = 'true'  # 必须是字符串的"true",不能是bool的True

    # 如果下面头部中指定的方法不包含当前请求的method，那么浏览器将不会交付给第三方网站
    # 1. 该HEADER不针对GET、HEAD、POST、OPTIONS这4个方法，这几个方法如果满足"简单跨域请求"的要求，那么浏览器可以直接访问，不需要发出OPTIONS请求。
    # 2. PUT、DELETE、PATCH这三个方法，会先发出OPTIONS请求，然后根据OPTIONS请求中的Access-Control-Allow-Methods,
    #    来决定是否发出这个方法的请求.  如果当前METHOD不包含在内，浏览器不会发出请求。
    #     见: https://segmentfault.com/q/1010000005067552
    # 3. 区分大小写，存在多个时使用 ',' 分割
    # response.headers['Access-Control-Allow-Methods'] = request.method
    response.headers['Access-Control-Allow-Methods'] = ','.join(['PATCH', 'PUT', 'DELETE'])
    # response.headers['Access-Control-Allow-Methods'] = 'PATCH'

    # 当一个跨域请求发送简单跨域请求包括：请求方法为HEAD，GET，POST;
    # 请求头只有4个字段，Accept，Accept-Language，Content-Language，Last-Event-ID;
    # 如果设置了Content-Type，则其值只能是application/x-www-form-urlencoded,multipart/form-data,text/plain
    # 例如： 如果请求头中带了，Content-Type,且不是"简单跨域请求"中定义的那几个。 那么浏览器会先发出OPTIONS请求，来确定是否允许带上Content-Type
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    # 控制同类型请求的预检命令(OPTIONS)结果的缓存时间，用以提升性能，单位:秒
    response.headers['Access-Control-Max-Age'] = '3600'

    return response

@app.route('/setcookie')
def set_cookie():
    print request.headers
    print request.method
    print request.cookies

    response = Response()
    response.set_cookie('testkey', 'testvalue')
    response.set_data('set cookie')

    return response

@app.route('/ping', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ping():
    response = Response()
    response.set_data('pong')

    return response
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
