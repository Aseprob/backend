"""
Module that implements JWT for the app
"""
from functools import wraps

import jwt
from flask import current_app, request


def create_token(user_id):
    """
    creates a jwt token
    """
    return jwt.encode({'user_id': str(user_id)},
                      current_app.config['SECRET_KEY'],
                      algorithm='HS256')


def token_required(f):
    """
    implements token validation
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {'message': 'Token is missing'}, 401
        try:
            jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except UnicodeDecodeError:
            return {'message': 'Token is invalid'}, 401
        return f(*args, **kwargs)
    return decorated
