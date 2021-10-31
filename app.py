from flask import Flask
from exec_engine import compile_run

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/<string:lang>')
def output(lang):
    return compile_run(lang)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
