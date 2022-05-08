import json
import scraper


def get_all_stations():
    file = open('stations.json')
    file_data = json.load(file)
    file.close()
    return {
        'code': 200,
        'result': file_data
    }


def get_station_by_id(id):
    file = open('stations.json')
    file_data = json.load(file)
    file.close()
    for station in file_data:
        if station['stationId'] == id:
            return {
                'code': 200,
                'result': station
            }

    return {
        'code': 404,
        'msg': 'No station with ID {} found'.format(id)
    }


def get_station_weather(id):
    data = scraper.get_station_data(id)
    return {
        'code': 200,
        'result': data
    }
