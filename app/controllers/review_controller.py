from flask import request, jsonify
from ..services import review_service
from ..schemas import review_schema, reviews_schema


def create_review():
    # Let ValidationError bubble to the global handler
    data = review_schema.load(request.get_json() or {})
    review = review_service.create_review(data)
    return jsonify(review_schema.dump(review)), 201


def list_reviews_for_place(place_id):
    reviews = review_service.get_reviews_for_place(place_id)
    return jsonify(reviews_schema.dump(reviews)), 200


def get_review(review_id):
    r = review_service.get_review(review_id)
    return jsonify(review_schema.dump(r)), 200


def update_review(review_id):
    data = review_schema.load(request.get_json() or {}, partial=request.method == 'PATCH')
    r = review_service.update_review(review_id, data)
    return jsonify(review_schema.dump(r)), 200


def delete_review(review_id):
    review_service.delete_review(review_id)
    return ('', 204)