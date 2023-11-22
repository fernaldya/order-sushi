from order import place_order
# from food import Food
from flask import request, Flask, jsonify

app = Flask(__name__)

orders = []


@app.route('/')
def home():
    return orders

@app.route('/order/{food}/{}')
def add_order():
    data = request.json
    place