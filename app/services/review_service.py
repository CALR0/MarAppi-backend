
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


def get_review(review_id):
    r = Review.query.get(review_id)
    if not r:
        raise NotFoundError('Review not found')
    return r


def update_review(review_id, data):
    r = Review.query.get(review_id)
    if not r:
        raise NotFoundError('Review not found')

    if 'content' in data:
        r.content = data.get('content')

    if 'rating' in data:
        r.rating = int(data.get('rating'))

    if 'place_id' in data:
        place = Place.query.get(data.get('place_id'))
        if not place:
            raise NotFoundError('Place not found')
        r.place_id = data.get('place_id')

    db.session.commit()
    return r


def delete_review(review_id):
    r = Review.query.get(review_id)
    if not r:
        raise NotFoundError('Review not found')

    db.session.delete(r)
    db.session.commit()
    return True