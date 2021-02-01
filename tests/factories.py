import factory
from faker import Faker

from author.models import Author
from book.models import Book, Genre
from manage import db

faker = Faker()


class BookFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Book
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    title = faker.sentence()
    subtitle = faker.sentence()
    description = faker.text()
    publication_date = faker.date()
    isbn = faker.isbn13()


class AuthorFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Author
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    given_name = faker.first_name()
    family_name = faker.last_name()


class GenreFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Genre
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = "technical"
