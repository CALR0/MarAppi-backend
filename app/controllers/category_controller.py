from flask import request, jsonify
from ..services import category_service


def create_category():
    data = request.get_json() or {}
    try:
        category = category_service.create_category(data)
        return jsonify(category.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


def list_categories():
    cats = category_service.get_all_categories()
    return jsonify([c.to_dict() for c in cats])