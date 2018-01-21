from flask import Flask, request, jsonify
from datetime import datetime
from dbmanager import DBManager

app = Flask(__name__)
db = DBManager()


@app.route('/data', methods=['GET', 'POST'])
def data():
    response = {'error': None}
    if request.method == 'GET':
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        id = request.args.get('id')

        check_date(from_date)
        check_date(to_date)
        check_id(id)

        results = db.retrieve(id, from_date, to_date)

        response['id'] = id
        response['data'] = results

    elif request.method == 'POST':
        json_data = request.get_json()
        if 'id' not in json_data or 'data' not in json_data:
            raise Exception('id and data must be specified.')

        data = process_data(json_data['id'], json_data['data'])

        db.store(data)

    return jsonify(response)


@app.route('/info', methods=['GET'])
def info():
    zones = db.list_ids()
    response = {'count': len(zones), 'zones': zones}

    return jsonify(response)


@app.errorhandler(500)
def error_handler(ex):
    return jsonify({'error': str(ex)})


def check_date(date):
    datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")


def check_id(id):
    if not id:
        raise Exception("id cannot be empty")


def process_data(id, data):
    check_id(id)
    ret = []
    for d in data:
        check_date(d['time'])
        ret.append([id, d.get('time'), d.get('temperature'), d.get('humidity')])

    return ret
