from flask import Blueprint,Flask, jsonify, json, request
from app.main.orders import orders

app = Flask(__name__)
app.register_blueprint(order)

users = Blueprint('order',__name__)

orders = []

@order.route("/order", methods=['POST'])
def order():
   global orders
   # name_of_food, price, quantity, restaurant
   userdata = request.get_json()
   try:
        name = userdata['name']
        price = userdata['price']
        quantity = userdata['quantity']
        location = userdata['location']

   except KeyError as item:
       return jsonify({'message': str(item)+'missing'}), 400

   new_order = {
       'name_of_food': name,
       'price': price,
       'quantity': quantity,
       'location': location
   }

   orders.append(new_order)
   return jsonify({"message": "order created"}), 201


@order.route('/order', methods=['GET'])
def get_order():
   return jsonify({'orders': orders}), 200

