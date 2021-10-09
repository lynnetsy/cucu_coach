from flask import Flask, jsonify
from helpers.wod_generator import wod_generator


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index page'


@app.route('/random-wod')
def randomwod_index():
    wod = wod_generator()
    return jsonify(wod), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
