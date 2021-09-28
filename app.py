from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    # print("test new values4")
    return render_template('index.html')
    # return 'Hello from flask application!'


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory("/src/static", filename)



if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True, host='0.0.0.0', port=8000)
