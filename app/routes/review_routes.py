from flask import Blueprint
from ..controllers.review_controller import create_review, list_reviews_for_place

bp = Blueprint('reviews', __name__, url_prefix='/api/reviews')

bp.route('', methods=['POST'])(create_review)
bp.route('/place/<int:place_id>', methods=['GET'])(list_reviews_for_place)
