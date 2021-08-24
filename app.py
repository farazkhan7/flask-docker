from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # print("test new values4")
    return 'Hello from flask application!'


if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True, host='0.0.0.0', port=8000)
