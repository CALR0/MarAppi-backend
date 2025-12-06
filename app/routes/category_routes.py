from flask import Blueprint
from ..controllers.category_controller import create_category, list_categories

bp = Blueprint('categories', __name__, url_prefix='/api/categories')

bp.route('', methods=['POST'])(create_category)
bp.route('', methods=['GET'])(list_categories)