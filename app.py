from flask import Flask, jsonify
import bl
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import waitress
import os


RATE_LIMIT_DAILY = os.getenv('RATE_LIMIT_DAILY')
RATE_LIMIT_HOURLY = os.getenv('RATE_LIMIT_HOURLY')

if RATE_LIMIT_DAILY is None:
    RATE_LIMIT_DAILY = 20

if RATE_LIMIT_HOURLY is None:
    RATE_LIMIT_HOURLY = 5


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["{} per day".format(
        RATE_LIMIT_DAILY), "{} per hour".format(RATE_LIMIT_HOURLY)]
)


@app.route('/station/<string:id>')
def get_station(id):
    if id == 'all':
        result = bl.get_all_stations()
    else:
        result = bl.get_station_by_id(int(id))

    return jsonify(result), result['code']


@app.route('/weather/<int:id>')
def get_station_weather(id):
    result = bl.get_station_weather(id)
    return jsonify(result), result['code']


if __name__ == '__main__':
    # Uncomment the waitress line and
    # comment the flask (app.run) line
    # on a production environment,
    # or vice versa.

    waitress.serve(app, host='0.0.0.0', port=1875)
    # app.run(host='0.0.0.0', port=1875)
