
from ..extensions import db
from ..models.review import Review
from ..models.place import Place
from ..errors import NotFoundError


def create_review(data):
    content = data.get('content')
    rating = data.get('rating')
    place_id = data.get('place_id')
    if not content or rating is None or not place_id:
        raise ValueError('content, rating and place_id are required')

    place = Place.query.get(place_id)
    if not place:
        raise NotFoundError('Place not found')

    review = Review(content=content, rating=int(rating), place_id=place_id)
    db.session.add(review)
    db.session.commit()
    return review


def get_reviews_for_place(place_id):
    return Review.query.filter_by(place_id=place_id).all()