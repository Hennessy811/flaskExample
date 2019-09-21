from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
@cross_origin()
def hello_world():
    return app.send_static_file('res.json')


if __name__ == '__main__':
    app.run()
