from flask import Flask, jsonify, request, json

app = Flask(__name__)

orders = []

users_list = []

loggedinuser = []

# routes for the api


@app.route('/api/v1/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data['username']
    password = data['password']
    role = data['role']

    try:
        username = data['username']
        password = data['password']
        role = data['role']

    except KeyError as item:
        return jsonify({'message': str(item)+'missing'}), 400

    users = {
        'username': username,
        'password': password,
        'role': role
    }
    users_list.append(users)

    for users in users_list:

        if not len(username) > 0:
            return jsonify({"message": "username can't be blank"}), 400

        if not len(password) > 0:
            return jsonify({"message": "password can't be blank"}), 400
        
        if not len(role) > 0:
            return jsonify({"message": "role can't be blank"}), 400

        else:
            return jsonify({"message": "Account created successfully", 'users': users_list}), 200

# Login
@app.route('/api/v1/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data['username']
    password = data['password']
    role = data['role']

    try:
        username = data['username']
        password = data['password']
        role = data['role']

    except KeyError as item:
        return jsonify({'message': str(item)+'missing'}), 400

    users = {
        'username': username,
        'password': password,
        'role': role
    }

    for users in users_list:

        if not len(username) > 0 and not len(password) > 0 and not len(role) > 0:
            return jsonify({"message":"fields can't be blank"}), 400

        if username == username and password == password and role == role:
            return jsonify({"message": "login successful"}), 200
        
        if username != username and password != password and role != role:
                return jsonify({"message": "invalid"})

        else:
           return jsonify({"message":"invalid"})
            


@app.route('/api/v1/session', methods=['POST'])
def session():

    username = []
    optiondata = request.get_json()

    option = optiondata["your option"]
    if option == "logout":
        return jsonify({"message": "you are logged out"}), 200

    elif option == "view orders":
        return order()


@app.route('/api/v1/order', methods=['POST'])
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


@app.route('/api/v1/order', methods=['GET'])
def get_order():
   return jsonify({'orders': orders}), 200


if __name__ == '__main__':
    app.run(debug=True)
