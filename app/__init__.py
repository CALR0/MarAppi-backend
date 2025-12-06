from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate, swagger

# Exceptions
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from .errors import APIError


def create_app():
    """Flask application factory.

    - Initializes Flask
    - Configures SQLAlchemy
    - Registers blueprints (expects each route module to expose `bp`)
    - Creates tables if they don't exist
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    # Initialize Swagger (Flasgger) with a minimal OpenAPI template
    try:
        template = {
            "openapi": "3.0.2",
            "info": {
                "title": "MarAppi API",
                "version": "1.0.0",
                "description": "API documentation for MarAppi backend"
            }
        }
        swagger.init_app(app, template=template)
    except Exception:
        # If Flasgger isn't configured or available, don't crash app startup
        pass
    # Ensure models are imported so Alembic/autogenerate can see SQLAlchemy metadata
    # Use a relative import to avoid shadowing the `app` variable.
    from . import models  # noqa: F401
    # Defensive: ensure app.extensions is a dict (some import setups may shadow it)
    if not isinstance(getattr(app, 'extensions', None), dict):
        app.extensions = {}
    migrate.init_app(app, db)

    # Import blueprints (each route module must expose `bp`)
    from .routes.category_routes import bp as categories_bp
    from .routes.place_routes import bp as places_bp
    from .routes.review_routes import bp as reviews_bp

    app.register_blueprint(categories_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)

    # Register global error handlers
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        # err.messages is a dict of field -> [errors]
        return jsonify({'errors': err.messages}), 400

    @app.errorhandler(APIError)
    def handle_api_error(err):
        return jsonify(err.to_dict()), err.status_code

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(err):
        # Basic mapping for common DB constraint errors
        return jsonify({'error': 'Database integrity error'}), 400

    @app.errorhandler(Exception)
    def handle_exception(err):
        # Don't leak internals
        # You might want to log the exception here
        return jsonify({'error': 'Internal server error'}), 500

    # Note: using Flask-Migrate for schema migrations. Do not use db.create_all()
    # in production; use the `flask db` commands instead.

    return app