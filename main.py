from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index page'


@app.route('/random-wod')
def randomwod_index():
    return jsonify({
        'title': 'Wod del 9 de octubre',
        'description': 'mortal legs cardio',
        'name': None,
        'type': 'for_time',
        'time': 900,
        'rounds': 3,
        'exercises': [
            {
                'name': 'burpee',
                'reps': 20,
            },
            {
                'name': 'clean',
                'reps': 10,
                'weight': 90,
                'unit': 'lbs',
        
            }

        ]
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
