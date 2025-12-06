from flask import request, jsonify
from ..services import place_service


def create_place():
    data = request.get_json() or {}
    try:
        place = place_service.create_place(data)
        return jsonify(place.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


def list_places():
    places = place_service.get_all_places()
    return jsonify([p.to_dict() for p in places])