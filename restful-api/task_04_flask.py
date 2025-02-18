#!/usr/bin/python3
"""
The module `flask`
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"},
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"}
}

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route("/data")
def get_users():
    """Return the lisdt of usernames as JSON"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Return user data if found"""
    return jsonify({"status": "OK"})

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error":"User not found"}), 404

@app.route("/status")
def add_user():
    """Add a new user"""
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = data
    return jsonify ({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
