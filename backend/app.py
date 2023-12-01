from order import place_order
# from food import Food
import os
from flask import request, Flask, jsonify
from database import DatabaseHandler
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
db_handler = DatabaseHandler(os.environ['DB_HOST'], os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_NAME'], int(os.environ['DB_PORT']))

@app.route('/')
def home():
    data = db_handler.fetch_data('SELECT * FROM sessions')
    return str(data)

@app.route('/ping')
def ping():
    return {'message': 'pong!'}

@app.route('/order/{food}/{}')
def add_order():
    data = request.json
    place
