from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.database import get_db
from app.services.auth import token_required
from bson import ObjectId

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('', methods=['GET'])
@token_required
def get_products():
    db = get_db()
    products = [Product.from_dict(product).to_dict() for product in db.products.find()]
    return jsonify(products), 200

@bp.route('', methods=['POST'])
@token_required
def create_product():
    db = get_db()
    data = request.json
    new_product = Product(company=data['company'], description=data['description'])
    result = db.products.insert_one(new_product.__dict__)
    new_product._id = result.inserted_id
    return jsonify(new_product.to_dict()), 201

@bp.route('/<product_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def product_operations(product_id):
    db = get_db()
    product = db.products.find_one({'_id': ObjectId(product_id)})
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    if request.method == 'GET':
        return jsonify(Product.from_dict(product).to_dict()), 200

    elif request.method == 'PUT':
        data = request.json
        updated_product = Product(company=data['company'], description=data['description'], _id=ObjectId(product_id))
        db.products.replace_one({'_id': ObjectId(product_id)}, updated_product.__dict__)
        return jsonify(updated_product.to_dict()), 200

    elif request.method == 'DELETE':
        db.products.delete_one({'_id': ObjectId(product_id)})
        return '', 204