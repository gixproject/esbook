import logging

from faker import Faker
from flask_script import Command, Option

from author.models import Author
from author.services import save_author_to_es
from book.models import Book, Genre
from book.services import save_book_to_es

logger = logging.getLogger(__name__)


class TestData(Command):
    option_list = (
        Option("--count", "-c", dest="count", default=50, type=int),
    )

    def run(self, count):
        """
        Creates test records.
        """
        faker = Faker()

        for _ in range(count):
            book = Book(
                title=faker.sentence(), subtitle=faker.sentence(), type="Book", publication_date=faker.date(),
                description=faker.text(), isbn=faker.isbn13(), pages=faker.random_number(), price=faker.random_number(),
                publisher=faker.word(),
            )

            for _ in range(faker.random_digit()):
                author = Author(given_name=faker.first_name(), family_name=faker.last_name())
                author.save()
                save_author_to_es(author)
                book.authors.append(author)

            genre = Genre.get_or_create(name="fake")
            book.genres.append(genre)

            book.save()
            save_book_to_es(book)

        logger.info('Test data was successfully created.')
