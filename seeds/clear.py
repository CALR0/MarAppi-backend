"""Clear seed data script for MarAppi.

Usage:

  set FLASK_APP=app:create_app
  python -m seeds.clear

This script deletes rows from `reviews`, `places` and `categories` in that
order using SQLAlchemy within the app context. It is intended for
development/testing only.
"""

from app import create_app
from app.extensions import db
from app.models import Review, Place, Category


def clear():
    app = create_app()
    with app.app_context():
        # Delete dependents first
        db.session.query(Review).delete()
        db.session.query(Place).delete()
        db.session.query(Category).delete()
        db.session.commit()
        print("Cleared seed data: reviews, places, categories")


if __name__ == "__main__":
    clear()
