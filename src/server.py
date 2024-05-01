# coding: utf-8
import os
import json
import sqlite3
from redis import Redis

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from flask import Flask, jsonify, request, send_from_directory, render_template, g

import messenger
from config import CONFIG
from fbpage import page

app = Flask(__name__)


def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis


def get_db_connection():
    conn = sqlite3.connect("./data/service.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/add_new_page', methods=['POST', 'GET'])
def add_new_page():
    if request.method == 'POST':
        data = request.data
        data = json.loads(data.decode('utf-8'))
        print(data)

        page_id = data.get('page_id')
        token = data.get('token')

        if not page_id or not token:
            return jsonify({'error': 'Sender ID and Page Token are required'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO page (page_id, token) VALUES (%s, %s)" % (page_id, token))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Page added successfully'}), 201

    return 'Hello World', 200


@app.route('/webhook', methods=['GET'])
def validate():
    if request.args.get('hub.mode', '') == 'subscribe' and \
                    request.args.get('hub.verify_token', '') == CONFIG['VERIFY_TOKEN']:

        print("Validating webhook")

        return request.args.get('hub.challenge', '')
    else:
        return 'Failed validation. Make sure the validation tokens match.'


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.data
    body = json.loads(data.decode('utf-8'))
    if 'object' in body and body['object'] == 'page':
        entries = body['entry']
        for entry in entries:
            message_event = json.dumps(entry['messaging'][0])
            redis = get_redis()
            redis.rpush('data', message_event)
    # payload = request.get_data(as_text=True)
    # print(payload)

    # redis = get_redis()
    # msg_data = json.dumps(payload)
    # redis.rpush('data', msg_data)

    # conn = get_db_connection()
    # cusor = conn.cursor()
    
    # page.handle_webhook(payload)

    return "ok"


@app.route('/authorize', methods=['GET'])
def authorize():
    account_linking_token = request.args.get('account_linking_token', '')
    redirect_uri = request.args.get('redirect_uri', '')

    auth_code = '1234567890'

    redirect_uri_success = redirect_uri + "&authorization_code=" + auth_code

    return render_template('authorize.html', data={
        'account_linking_token': account_linking_token,
        'redirect_uri': redirect_uri,
        'redirect_uri_success': redirect_uri_success
    })


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3105, debug=True, threaded=True)
