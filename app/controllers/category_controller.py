from flask import request, jsonify
from ..services import category_service
from ..schemas import category_schema, categories_schema


def create_category():
        """
        Create a new category
        ---
        tags:
            - Categories
        requestBody:
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            name:
                                type: string
                        required:
                            - name
        responses:
            201:
                description: Created
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                id:
                                    type: integer
                                name:
                                    type: string
        """
        # Let ValidationError bubble to the global handler
        data = category_schema.load(request.get_json() or {})
        category = category_service.create_category(data)
        return jsonify(category_schema.dump(category)), 201


def list_categories():
        """
        List categories
        ---
        tags:
            - Categories
        responses:
            200:
                description: OK
                content:
                    application/json:
                        schema:
                            type: array
                            items:
                                type: object
                                properties:
                                    id:
                                        type: integer
                                    name:
                                        type: string
        """
        cats = category_service.get_all_categories()
        return jsonify(categories_schema.dump(cats)), 200
 

def get_category(category_id):
        """
        Get a category by id
        ---
        tags:
            - Categories
        parameters:
            - in: path
                name: category_id
                schema:
                    type: integer
                required: true
                description: Numeric ID of the category to get
        responses:
            200:
                description: OK
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                id:
                                    type: integer
                                name:
                                    type: string
            404:
                description: Not Found
        """
        cat = category_service.get_category(category_id)
        return jsonify(category_schema.dump(cat)), 200


def update_category(category_id):
    # For PUT expect full payload; for PATCH allow partial
    data = category_schema.load(request.get_json() or {}, partial=request.method == 'PATCH')
    cat = category_service.update_category(category_id, data)
    return jsonify(category_schema.dump(cat)), 200


def delete_category(category_id):
    category_service.delete_category(category_id)
    return ('', 204)