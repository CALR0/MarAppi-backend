from marshmallow import Schema, fields, validate


class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1))
    rating = fields.Int(required=True, validate=validate.Range(min=1, max=5))
    place_id = fields.Int(required=True)
