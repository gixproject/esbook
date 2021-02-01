import logging

from flask_script import Command

from author.services import save_author_to_es
from book.models import Book
from book.services import save_book_to_es

logger = logging.getLogger(__name__)


class MigrateBooks(Command):
    def run(self):
        """
        Migrates books and their authors to ElasticSearch.
        """
        try:
            for book in Book.query.all():
                save_book_to_es(book)

                for author in book.authors.all():
                    save_author_to_es(author)
        except Exception as exc:
            logger.error(exc)

        logger.info(
            "Books and their authors were successfully migrated to ElasticSearch."
        )
