from flask import request, jsonify
from ..services import place_service
from ..schemas import place_schema, places_schema


def create_place():
    # Let ValidationError bubble to the global handler
    data = place_schema.load(request.get_json() or {})
    place = place_service.create_place(data)
    return jsonify(place_schema.dump(place)), 201


def list_places():
    places = place_service.get_all_places()
    return jsonify(places_schema.dump(places)), 200


def get_place(place_id):
    p = place_service.get_place(place_id)
    return jsonify(place_schema.dump(p)), 200


def update_place(place_id):
    data = place_schema.load(request.get_json() or {}, partial=request.method == 'PATCH')
    p = place_service.update_place(place_id, data)
    return jsonify(place_schema.dump(p)), 200


def delete_place(place_id):
    place_service.delete_place(place_id)
    return ('', 204)