from flask import Blueprint
from ..controllers.review_controller import (
	create_review,
	list_reviews_for_place,
	get_review,
	update_review,
	delete_review,
)

bp = Blueprint('reviews', __name__, url_prefix='/api/reviews')

bp.route('', methods=['POST'])(create_review)
bp.route('/place/<int:place_id>', methods=['GET'])(list_reviews_for_place)

# Single resource routes
bp.route('/<int:review_id>', methods=['GET'])(get_review)
bp.route('/<int:review_id>', methods=['PUT'])(update_review)
bp.route('/<int:review_id>', methods=['PATCH'])(update_review)
bp.route('/<int:review_id>', methods=['DELETE'])(delete_review)
