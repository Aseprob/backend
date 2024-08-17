"""
Endpoint with full crud operations for the client route
"""
from bson import ObjectId
from flask import Blueprint, jsonify, request

from app.database import get_db
from app.models.client import Client
from app.services.auth import token_required, token_required_with_context

bp = Blueprint('clients', __name__, url_prefix='/clients')


@bp.route('', methods=['GET'])
@token_required
# TODO: make search limited to the current user's index_id(s), that way a single user can work on more than one group. 
# without being able to see othe user's info
#
# @token_required_with_context
# def get_clients(current_user):
def get_clients():
    """
    Returns all clients
    """
    db = get_db()
    clients = [Client.from_dict(client).to_dict()
               for client in db.clients.find()]
    return jsonify(clients), 200


@bp.route('', methods=['POST'])
@token_required
def create_client():
    """
    Creates a client
    """
    db = get_db()
    data = request.json
    new_client = Client(email=data['email'], notes=data.get('notes'))
    result = db.clients.insert_one(new_client.__dict__)
    new_client = result.inserted_id
    return jsonify(new_client.to_dict()), 201


@bp.route('/<client_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def client_operations(client_id):
    """
    Operations to interact with a specific client
    """
    db = get_db()
    client = db.clients.find_one({'_id': ObjectId(client_id)})
    if not client:
        return jsonify({'message': 'Client not found'}), 404

    if request.method == 'GET':
        return jsonify(Client.from_dict(client).to_dict()), 200

    elif request.method == 'PUT':
        data = request.json
        updated_client = Client(email=data['email'], notes=data.get(
            'notes'), _id=ObjectId(client_id))
        db.clients.replace_one(
            {'_id': ObjectId(client_id)}, updated_client.__dict__)
        return jsonify(updated_client.to_dict()), 200

    elif request.method == 'DELETE':
        db.clients.delete_one({'_id': ObjectId(client_id)})
        return '', 204
