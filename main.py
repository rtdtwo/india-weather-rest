from flask import Flask, jsonify
import bl

app = Flask(__name__)


@app.route('/station/<string:id>')
def get_station(id):
    if id == 'all':
        result = bl.get_all_stations()
    else:
        result = bl.get_station_by_id(int(id))

    return jsonify(result), result['code']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1875)
