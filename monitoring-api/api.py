from flask import Flask, request, jsonify
from dbmanager import DBManager

app = Flask(__name__)
db = DBManager()


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        id = request.args.get('id')
        # retrieve and return data

    elif request.method == 'POST':
        pass # store new data

    return ""


@app.route('/info', methods=['GET'])
def info():
    zones = db.list_ids()
    response = {'count': len(zones), 'zones': zones}

    return jsonify(response)


@app.errorhandler(500)
def error_handler(ex):
    return jsonify({'error': str(ex)})
