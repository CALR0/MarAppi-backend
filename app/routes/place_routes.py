from flask import Blueprint
from ..controllers.place_controller import (
	create_place,
	list_places,
	get_place,
	update_place,
	delete_place,
)

bp = Blueprint('places', __name__, url_prefix='/api/places')

bp.route('', methods=['POST'])(create_place)
bp.route('', methods=['GET'])(list_places)

# Single resource routes
bp.route('/<int:place_id>', methods=['GET'])(get_place)
bp.route('/<int:place_id>', methods=['PUT'])(update_place)
bp.route('/<int:place_id>', methods=['PATCH'])(update_place)
bp.route('/<int:place_id>', methods=['DELETE'])(delete_place)