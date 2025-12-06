from flask import request, jsonify
from marshmallow import ValidationError
from ..services import category_service
from ..schemas import category_schema, categories_schema


def create_category():
    try:
        data = category_schema.load(request.get_json() or {})
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    try:
        category = category_service.create_category(data)
        return jsonify(category_schema.dump(category)), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


def list_categories():
    cats = category_service.get_all_categories()
    return jsonify(categories_schema.dump(cats)), 200