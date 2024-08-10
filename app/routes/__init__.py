"""
Easy imports for the routes
"""
from .client_routes import bp as client_bp
from .product_routes import bp as product_bp
from .order_routes import bp as order_bp

blueprints = [client_bp, product_bp, order_bp]
