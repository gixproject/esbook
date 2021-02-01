import logging

from elasticsearch.exceptions import TransportError
from flask import current_app

from author.services import save_author_to_es
from book.schemes import BookElasticSchema
from search.services import ElasticSearch

logger = logging.getLogger(__name__)


def save_book_to_es(book) -> None:
    """
    Stores a`Book` instance into ElasticSearch.
    :param Author book: A `Book` instance.
    """
    if not book.authors.count():
        logger.warning(
            f"Book with id {book.id} has no authors. "
            f"It can't be saved in ElasticSearch."
        )
        return

    es_client = ElasticSearch()

    try:
        es_client.index(
            index=current_app.config["ELASTIC_BOOKS_INDEX"],
            body=BookElasticSchema().dump(book),
            id=book.id,
        )

        for author in book.authors.all():
            save_author_to_es(author)

    except TransportError as exc:
        logger.error("Transport error. Invalid mapping.", exc)
