#!/usr/bin/python3
"""API security with Basic Auth and JWT."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "change-this-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth username and password."""
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
    return None


@auth.error_handler
def auth_error(status):
    """Return 401 for Basic Auth errors."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    """Return 401 when JWT token is missing."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """Return 401 when JWT token is invalid."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """Return 401 when JWT token is expired."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    """Return 401 when JWT token is revoked."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_callback(jwt_header, jwt_payload):
    """Return 401 when fresh JWT token is required."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login route that returns a JWT access token."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Bad credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Bad credentials"}), 401

    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Protected route only accessible by admin users."""
    username = get_jwt_identity()

    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
