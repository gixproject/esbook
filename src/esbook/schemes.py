from marshmallow import fields, Schema


class PaginatedSchema(Schema):
    page = fields.Integer()
    pages_count = fields.Integer()
    per_page = fields.Integer()
    count = fields.Integer()
