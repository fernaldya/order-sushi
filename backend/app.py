import os
from flask import request, Flask, jsonify
from database import DatabaseHandler
from dotenv import load_dotenv
from session import Session

app = Flask(__name__)
load_dotenv()
db_handler = DatabaseHandler(os.environ['DB_HOST'], os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_NAME'], int(os.environ['DB_PORT']))

@app.route('/ping')
def ping():
    return {'message': 'pong!'}

@app.route('/sessions')
def home():
    data = Session(db_handler).all()
    return jsonify(sessions=list(map(lambda x: x.serialize(), data)))

@app.route('/sessions/<id>', methods=['GET'])
def get_session(id):
    data = Session(db_handler).find(int(id))
    if data:
        return jsonify(data.serialize()), 200
    else:
        return jsonify(None), 404
