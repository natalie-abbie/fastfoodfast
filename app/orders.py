from flask import Blueprint, Flask, jsonify, json, request

orders = Blueprint('order',__name__)

orders_list = []

@orders.route("/order", methods=['POST'])
def post_order():
   global orders_list
   # name_of_food, price, quantity, restaurant
   userdata = request.get_json()
   try:
        name = userdata['name']
        price = userdata['price']
        quantity = userdata['quantity']
        location = userdata['location']

   except KeyError as item:
       return jsonify({'message': str(item) + 'missing'}), 400

   new_order = {
       'name_of_food': name,
       'price': price,
       'quantity': quantity,
       'location': location
   }

   orders_list.append(new_order)
   return jsonify({"message": "order created"}), 201


@orders.route('/order', methods=['GET'])
def get_order():
    if len(orders_list) == 0:
        return jsonify({"message":"No orders found"})
    return jsonify({'orders': orders_list}), 200
