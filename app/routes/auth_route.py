# app/routes/auth_routes.py
"""
Endpoint to obtain JWT token
"""
from flask import Blueprint, jsonify, request

from app.database import get_db
from app.services.auth import create_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/token', methods=['POST'])
def get_token():
    """
    Returns a JWT token when user credentials are correct.
    If user does not exist, creates a new profile.
    """
    db = get_db()
    data = request.json
    user = db.users.find_one({'email': data['email']})
    
    if not user:
        # Create new user profile if email does not exist in db
        user_id = db.users.insert_one({
            'email': data['email'],
            'password': data['password']
        }).inserted_id
        user = db.users.find_one({'_id': user_id})
    elif user['password'] != data['password']:
        # Return error if password is incorrect for existing user
        return jsonify({'message': 'Invalid credentials'}), 401

    token = create_token(user['_id'])
    return jsonify({'token': token}), 200
