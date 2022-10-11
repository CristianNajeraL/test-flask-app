from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'<h1>Test</h1>'

@app.route('/<name>')
def success(name):
   return f"Welcome {name}"


if __name__ == '__main__':
    app.run()
