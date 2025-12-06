"""Seed script to insert example data into the development database.

Run with:

  set FLASK_APP=app:create_app
  python -m seeds.seed

The script is idempotent: it deletes existing rows in `reviews`, `places`
and `categories` before inserting examples.
"""

from app import create_app
from app.extensions import db
from app.models import Category, Place, Review


def seed():
    app = create_app()
    with app.app_context():
        # Clear existing data (reviews -> places -> categories)
        Review.query.delete()
        Place.query.delete()
        Category.query.delete()
        db.session.commit()

        # Create categories
        beaches = Category(name="Beaches")
        historic = Category(name="Historic")
        nature = Category(name="Nature")
        db.session.add_all([beaches, historic, nature])
        db.session.commit()

        # Create places
        p1 = Place(
            name="Rodadero Beach",
            description="Sandy beach with calm waters and restaurants nearby.",
            category_id=beaches.id,
        )
        p2 = Place(
            name="Castillo de San Felipe",
            description="Historic fortress with panoramic views.",
            category_id=historic.id,
        )
        p3 = Place(
            name="Minca",
            description="Mountain village with waterfalls and hiking trails.",
            category_id=nature.id,
        )
        db.session.add_all([p1, p2, p3])
        db.session.commit()

        # Create reviews
        r1 = Review(content="Beautiful beach, very relaxing.", rating=5, place_id=p1.id)
        r2 = Review(content="Great views and history.", rating=4, place_id=p2.id)
        r3 = Review(content="Nice trails and coffee farms.", rating=5, place_id=p3.id)
        db.session.add_all([r1, r2, r3])
        db.session.commit()

        print("Seed complete: inserted categories, places and reviews.")


if __name__ == "__main__":
    seed()
