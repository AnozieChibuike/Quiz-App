from app import app
from flask import jsonify
from app import jwt


@app.errorhandler(404)
def page_not_found(error):
    # You can customize the response here
    print(10)
    return jsonify({"error": str(error)}), 404


# @app.errorhandler(500)
# def server_error(error):
#     print(error)
#     # You can customize the response here
#     return jsonify({"error": str(error)}), 500


@app.errorhandler(415)
def bad_content_type(error):
    return jsonify({"error": str(error)}), 415


@app.errorhandler(405)
def bad_method(error):
    return jsonify({"error": str(error)}), 415


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "The token has expired"}), 400


# Custom error handler for invalid tokens
@jwt.invalid_token_loader
def my_invalid_token_callback(error_string):
    return jsonify({"error": "Invalid token. Please log in again."}), 422


# Custom error handler for missing tokens
@jwt.unauthorized_loader
def my_missing_token_callback(error_string):
    return jsonify({"error": "Missing token. Please log in."}), 401
