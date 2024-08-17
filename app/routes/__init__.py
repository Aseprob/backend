"""
Easy imports for the routes
"""
from .auth_route import bp as auth_bp
from .client_routes import bp as client_bp
from .order_routes import bp as order_bp
from .product_routes import bp as product_bp

blueprints = [client_bp, product_bp, order_bp, auth_bp]
