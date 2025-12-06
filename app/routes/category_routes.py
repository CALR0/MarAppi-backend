from flask import Blueprint
from ..controllers.category_controller import (
	create_category,
	list_categories,
	get_category,
	update_category,
	delete_category,
)

bp = Blueprint('categories', __name__, url_prefix='/api/categories')

bp.route('', methods=['POST'])(create_category)
bp.route('', methods=['GET'])(list_categories)

# Single resource routes
bp.route('/<int:category_id>', methods=['GET'])(get_category)
bp.route('/<int:category_id>', methods=['PUT'])(update_category)
bp.route('/<int:category_id>', methods=['PATCH'])(update_category)
bp.route('/<int:category_id>', methods=['DELETE'])(delete_category)