#!/usr/bin/python3
"""
The module `flask`
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    """Return the list of usernames as JSON"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return user data if found"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user()", methods=["POST"])
def add_user():
    """Add a new user"""
    data = request.get_json()
    username = data.get("username")

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
