from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        id = request.args.get('id')
        # retrieve and return data

    elif request.method == 'POST':
        pass # store new data

    return ""
