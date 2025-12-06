from flask import request, jsonify
from ..services import category_service
from ..schemas import category_schema, categories_schema


def create_category():
    # Let ValidationError bubble to the global handler
    data = category_schema.load(request.get_json() or {})
    category = category_service.create_category(data)
    return jsonify(category_schema.dump(category)), 201


def list_categories():
    cats = category_service.get_all_categories()
    return jsonify(categories_schema.dump(cats)), 200