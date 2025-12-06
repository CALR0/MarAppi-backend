from flask import request, jsonify
from marshmallow import ValidationError
from ..services import review_service
from ..schemas import review_schema, reviews_schema


def create_review():
    try:
        data = review_schema.load(request.get_json() or {})
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    try:
        review = review_service.create_review(data)
        return jsonify(review_schema.dump(review)), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


def list_reviews_for_place(place_id):
    reviews = review_service.get_reviews_for_place(place_id)
    return jsonify(reviews_schema.dump(reviews)), 200