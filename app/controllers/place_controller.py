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