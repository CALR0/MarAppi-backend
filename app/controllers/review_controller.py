from flask import request, jsonify
from ..services import review_service


def create_review():
    data = request.get_json() or {}
    try:
        review = review_service.create_review(data)
        return jsonify(review.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


def list_reviews_for_place(place_id):
    reviews = review_service.get_reviews_for_place(place_id)
    return jsonify([r.to_dict() for r in reviews])