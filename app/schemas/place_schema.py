from marshmallow import Schema, fields, validate


class PlaceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(allow_none=True)
    category_id = fields.Int(required=True)
