from flask import request, jsonify
from marshmallow import ValidationError
from ..services import place_service
from ..schemas import place_schema, places_schema


def create_place():
    try:
        data = place_schema.load(request.get_json() or {})
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    try:
        place = place_service.create_place(data)
        return jsonify(place_schema.dump(place)), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


def list_places():
    places = place_service.get_all_places()
    return jsonify(places_schema.dump(places)), 200