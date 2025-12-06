from flask import Flask
from .config import Config
from .extensions import db


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

    # Import blueprints (each route module must expose `bp`)
    from .routes.category_routes import bp as categories_bp
    from .routes.place_routes import bp as places_bp
    from .routes.review_routes import bp as reviews_bp

    app.register_blueprint(categories_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)

    # Create DB tables when app starts (safe for simple apps)
    with app.app_context():
        db.create_all()

    return app