from sqlalchemy.dialects.postgresql import UUID

from author.models import Author
from db import db
from esbook.models_mixins import IdMixin, CreatedUpdatedMixin, CRUDMixin

book_authors = db.Table(
    "book_authors", db.metadata,
    db.Column("author_id", UUID(as_uuid=True), db.ForeignKey("author.id")),
    db.Column("book_id", UUID(as_uuid=True), db.ForeignKey("book.id"))
)

book_genres = db.Table(
    "book_genres", db.metadata,
    db.Column("genre_id", db.String(length=50), db.ForeignKey("genre.name")),
    db.Column("book_id", UUID(as_uuid=True), db.ForeignKey("book.id"))
)


class Genre(db.Model, CreatedUpdatedMixin, CRUDMixin):
    __tablename__ = "genre"

    name = db.Column(db.String(length=50), nullable=False, doc="Genre name", primary_key=True)


class Book(db.Model, IdMixin, CreatedUpdatedMixin, CRUDMixin):
    __tablename__ = "book"

    title = db.Column(db.String(length=256), nullable=False, doc="Book title")
    subtitle = db.Column(db.Text, nullable=False, doc="Book subtitle")
    isbn = db.Column(db.String(length=50), doc="ISBN", unique=True)
    issn = db.Column(db.String(length=50), doc="ISSN", unique=True)
    publisher = db.Column(db.String(length=255), doc="Publisher")
    type = db.Column(db.Text(), nullable=False, doc="The type of the book cover")
    publication_date = db.Column(db.Date, nullable=False, doc="Publication date")
    description = db.Column(db.Text, nullable=False, doc="Description")
    pages = db.Column(db.Integer, default=0, doc="Pages count")
    language = db.Column(db.String(length=50), doc="Language")
    price = db.Column(db.Integer, default=0, doc="Price")
    copyright = db.Column(db.String(length=50), doc="Copyright license")
    authors = db.relationship(
        Author, secondary=book_authors, backref=db.backref("books", lazy="dynamic"), lazy="dynamic",
    )
    genres = db.relationship(
        Genre, secondary=book_genres, backref=db.backref("books", lazy="dynamic"), lazy="dynamic",
    )

    def __repr__(self):
        return self.title

    @property
    def get_authors_names(self) -> list:
        """
        Returns a list of authors full names.
        """
        return [author.full_name for author in self.authors]

    @property
    def get_genres(self) -> list:
        """
        Returns a list of genres names.
        """
        return [genre.name for genre in self.genres]
