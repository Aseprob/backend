"""Module that starts the app."""
from flask import Flask, jsonify

from config import Config

from .database import close_db
from .routes import blueprints


def create_app():
    """
    creates the app
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register all blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Database connection teardown
    app.teardown_appcontext(close_db)

    # Optional: Add any app-wide configurations or initializations here

    @app.route('/health')
    def home():
        return jsonify({"msg": "If you can reach this, we are healthy!"})

    return app
