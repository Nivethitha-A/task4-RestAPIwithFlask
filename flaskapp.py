from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {
    1: {"id": 1, "name": "John", "email": "john@example.com"},
    2: {"id": 2, "name": "Sara", "email": "sara@example.com"}
}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

# GET single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users[new_id] = new_user
    return jsonify(new_user), 201

# PUT update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify(users[user_id])

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})

if __name__ == '__main__':
    app.run(debug=True)