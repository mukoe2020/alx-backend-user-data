#!/usr/bin/env python3
"""
create a flask app
"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect, url_for

app = Flask(__name__)
Auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """
    GET /
    Return: welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """
    POST /users
    Register a user
    Return: user email
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
