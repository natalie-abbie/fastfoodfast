from flask import Blueprint,Flask, jsonify, json, requests
from app.main.users import users

app = Flask(__name__)
app.register_blueprint(users)

users = Blueprint('users',__name__)


@users.route("/",methods=['GET'])

users_list = []

loggedinuser = []

# routes for the api

@users.route('/register', methods=['POST'])
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

        if not len(username) > 0 and not len(password) > 0 and not len(role) > 0:
            return jsonify({"message":"fields can't be blank"}), 400

        if username == username and password == password and role == role:
            return jsonify({"message": "login successful"}), 200
        
        if username != username and password != password and role != role:
                return jsonify({"message": "invalid"})

        else:
           return jsonify({"message":"invalid"})
            


@app.route('/session', methods=['POST'])
def session():

    username = []
    optiondata = request.get_json()

    option = optiondata["your option"]
    if option == "logout":
        return jsonify({"message": "you are logged out"}), 200

    elif option == "view orders":
        return order()
