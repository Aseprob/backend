"""
Module that implements JWT for the app
"""
import logging
from functools import wraps

import jwt
from flask import current_app, jsonify, request


def create_token(user_id):
    """
    creates a jwt token
    """
    return jwt.encode({'user_id': str(user_id)},
                      current_app.config['SECRET_KEY'],
                      algorithm='HS256')


def validate_token():
    """
    Validates the token from the request headers
    """
    token = None
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        logging.debug("Received Authorization header: %s", auth_header)
        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            logging.error("Malformed Authorization header")
            return None, (jsonify({'message': 'Token is missing or invalid'}), 401)

    if not token:
        return None, (jsonify({'message': 'Token is missing!'}), 401)

    try:
        logging.debug("Attempting to decode token: %s", token)
        data = jwt.decode(
            token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        current_user = data['user_id']
        return current_user, None
    except jwt.ExpiredSignatureError:
        return None, (jsonify({'message': 'Token has expired'}), 401)
    except jwt.InvalidTokenError as e:
        logging.error("Invalid token: %s", str(e))
        return None, (jsonify({'message': 'Token is invalid!'}), 401)


def token_required(f):
    """
    implements token validation
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        _, error = validate_token()
        if error:
            return error
        return f(*args, **kwargs)
    return decorated


def token_required_with_context(f):
    """
    implements token validation with user context
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user, error = validate_token()
        if error:
            return error
        return f(current_user, *args, **kwargs)
    return decorated
