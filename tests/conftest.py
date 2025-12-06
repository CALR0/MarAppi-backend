import pytest
import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so tests can import the app package
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import create_app
from app.extensions import db


@pytest.fixture(scope="function")
def app():
    """Create and configure a new app instance for each test."""
    # Force in-memory SQLite for tests
    os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # Create the database and the tables
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
