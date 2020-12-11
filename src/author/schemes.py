from flask import app
from flask_marshmallow import Marshmallow
from marshmallow import fields

from author.models import Author

ma = Marshmallow(app)


class AuthorModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        exclude = ("updated_at",)
        model = Author


class AuthorElasticSchema(AuthorModelSchema):
    source_id = fields.UUID(attribute="id")
    updated_at = fields.DateTime("%Y-%m-%d %H:%M:%S")

    class Meta:
        exclude = ("id", "created_at")
        model = Author
