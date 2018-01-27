from flask import Flask, request, jsonify
from datetime import datetime
from dbmanager import DBManager
import os

app = Flask(__name__)
db = DBManager(os.environ.get('DATABASE_PATH', 'monitored_data.db'))


@app.route('/data', methods=['GET', 'POST'])
def data():
    response = {'error': None}
    if request.method == 'GET':
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        zone = request.args.get('zone')

        check_date(from_date)
        check_date(to_date)
        check_zone(zone)

        results = db.retrieve(zone, from_date, to_date)

        response['zone'] = zone
        response['data'] = results

    elif request.method == 'POST':
        json_data = request.get_json()
        if 'zone' not in json_data or 'data' not in json_data:
            raise Exception('zone and data must be specified.')

        data = process_data(json_data['zone'], json_data['data'])

        db.store(data)

    return jsonify(response)


@app.route('/info', methods=['GET'])
def info():
    zones = db.list_zones()
    response = {'db': db.path, 'count': len(zones), 'zones': zones}

    return jsonify(response)


@app.errorhandler(500)
def error_handler(ex):
    return jsonify({'error': str(ex)}), 500


def check_date(date):
    datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")


def check_zone(name):
    if not name:
        raise Exception("zone cannot be empty")


def process_data(zone, data):
    check_zone(zone)
    ret = []
    for d in data:
        check_date(d['time'])
        ret.append([zone, d.get('time'), d.get('temperature'), d.get('humidity')])

    return ret
