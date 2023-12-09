import os
from flask import jsonify
from app import app
from models import Session
from services import DatabaseHandler

db_handler = DatabaseHandler(os.environ['DB_HOST'], os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_NAME'], int(os.environ['DB_PORT']))

@app.route('/ping')
def ping():
    return {'message': 'pong!'}

### Sessions
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
