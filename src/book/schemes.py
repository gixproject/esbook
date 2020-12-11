from apispec.ext.marshmallow import OpenAPIConverter
from apispec.utils import OpenAPIVersion
from flask import app
from flask_marshmallow import Marshmallow
from marshmallow import fields

from book.models import Book

ma = Marshmallow(app)


class BookModelSchema(ma.SQLAlchemyAutoSchema):
    authors = fields.Method("get_authors")
    genres = fields.Method("get_genres")

    def get_authors(self, book):
        return book.get_authors_names

    def get_genres(self, book):
        return book.get_genres

    class Meta:
        exclude = ("updated_at",)
        model = Book
        include_fk = True


class BookElasticSchema(BookModelSchema):
    source_id = fields.UUID(attribute="id")
    updated_at = fields.DateTime("%Y-%m-%d %H:%M:%S")

    class Meta:
        exclude = ("price", "copyright", "language", "id", "created_at", "type")
        model = Book
        include_fk = True


# JSON schema for a book
book_json_schema = OpenAPIConverter(
    OpenAPIVersion(openapi_version="2.0"), schema_name_resolver=None, spec=None
).schema2jsonschema(schema=BookModelSchema(exclude=("authors", "genres")))
book_json_schema["properties"]["authors"] = {
    "type": "array",
    "items": {"type": "string"},
}
book_json_schema["properties"]["genres"] = {
    "type": "array",
    "items": {"type": "string"},
}
