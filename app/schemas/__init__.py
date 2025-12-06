from .category_schema import CategorySchema
from .place_schema import PlaceSchema
from .review_schema import ReviewSchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

place_schema = PlaceSchema()
places_schema = PlaceSchema(many=True)

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

__all__ = [
    'category_schema', 'categories_schema',
    'place_schema', 'places_schema',
    'review_schema', 'reviews_schema',
]
