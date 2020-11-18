from flask import app
from flask_marshmallow import Marshmallow

from author.models import Author

ma = Marshmallow(app)


class AuthorModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        exclude = ("updated_at",)
        model = Author
        include_fk = True
