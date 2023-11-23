from order import place_order
# from food import Food
from flask import request, Flask, jsonify

app = Flask(__name__)

orders = []


@app.route('/')
def home():
    return orders

@app.route('/ping')
def ping():
    return {'message': 'pong!'}

@app.route('/order/{food}/{}')
def add_order():
    data = request.json
    place
