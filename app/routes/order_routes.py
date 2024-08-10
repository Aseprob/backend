from flask import Blueprint, request, jsonify
from app.models.order import Order
from app.database import get_db
from app.services.auth import token_required
from bson import ObjectId

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('', methods=['GET'])
@token_required
def get_orders():
    db = get_db()
    orders = [Order.from_dict(order).to_dict() for order in db.orders.find()]
    return jsonify(orders), 200

@bp.route('', methods=['POST'])
@token_required
def create_order():
    db = get_db()
    data = request.json
    new_order = Order(client_id=data['client_id'], product_id=data['product_id'])
    result = db.orders.insert_one(new_order.__dict__)
    new_order._id = result.inserted_id
    return jsonify(new_order.to_dict()), 201

@bp.route('/<order_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def order_operations(order_id):
    db = get_db()
    order = db.orders.find_one({'_id': ObjectId(order_id)})
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    if request.method == 'GET':
        return jsonify(Order.from_dict(order).to_dict()), 200

    elif request.method == 'PUT':
        data = request.json
        updated_order = Order(client_id=data['client_id'], product_id=data['product_id'], _id=ObjectId(order_id))
        db.orders.replace_one({'_id': ObjectId(order_id)}, updated_order.__dict__)
        return jsonify(updated_order.to_dict()), 200

    elif request.method == 'DELETE':
        db.orders.delete_one({'_id': ObjectId(order_id)})
        return '', 204