import logging

from flask_script import Command

from book.models import Book
from book.services import save_book_to_es

logger = logging.getLogger(__name__)


class MigrateBooks(Command):
    """
    Migrates books and their authors to ElasticSearch.
    """

    def run(self):
        try:
            for book in Book.query.all():
                save_book_to_es(book)
        except Exception as exc:
            logger.error(exc)

        logger.info(
            "Books and their authors were successfully migrated to ElasticSearch."
        )
