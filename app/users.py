from flask import Blueprint,Flask, jsonify, json, request

user = Blueprint('users', __name__)

users_list = []
loggedinuser = []

# routes for the api

@user.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data['username']
    email = data['email']
    contact = data['contact']
    role = data['role']
    password = data['password']

    try:
        username = data['username']
        email = data['email']
        contact = data['contact']
        role = data['role']
        password = data['password']

    except KeyError as item:
        return jsonify({'message': str(item)+'missing'}), 400

    users = {
        'username': username,
        'email': email,
        'contact': contact,
        'role': role,
        'password': password
    }
    users_list.append(users)

    for users in users_list:

        
    
        else:
            return jsonify({"message": "Account created successfully", 'users': users_list}), 200

# Login
@user.route('/login', methods=['POST'])
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

        if not len(username) > 0 and not len(email) > 0 and not len(contact) > 0 and not len(password) >0 and not len(role) >0:
            return jsonify({"message": "field can't be blank"}), 400

        if username == username and password == password and role == role:
            return jsonify({"message": "login successful"}), 200
        
        if username != username and password != password and role != role:
                return jsonify({"message": "invalid"})

        else:
           return jsonify({"message":"invalid"})
            


@user.route('/session', methods=['POST'])
def session():

    username = []
    optiondata = request.get_json()

    option = optiondata["your option"]
    if option == "logout":
        return jsonify({"message": "you are logged out"}), 200

    elif option == "view orders":
        return order()
