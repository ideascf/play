from flask import Flask

app = Flask(__name__)


@app.route('/<page>')
def main(page):
    # Got page, it's type is str
    print(page, type(page))

    # so should use %s but not %d
    return 'You request page is %s' % page

if __name__ == '__main__':
    app.run()
