from flask import Blueprint
from ..controllers.place_controller import create_place, list_places

bp = Blueprint('places', __name__, url_prefix='/api/places')

bp.route('', methods=['POST'])(create_place)
bp.route('', methods=['GET'])(list_places)