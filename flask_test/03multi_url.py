from flask import Flask

app = Flask(__name__)

@app.route('/main')
@app.route('/')
def main():
    return 'hello 03'

if __name__ == '__main__':
    app.run()
