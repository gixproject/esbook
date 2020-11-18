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
