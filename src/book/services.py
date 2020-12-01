import logging

from elasticsearch.exceptions import TransportError
from flask import current_app

from book.schemes import BookElasticSchema
from search.services import ElasticSearchObject

logger = logging.getLogger(__name__)


def save_book_to_es(book) -> None:
    """
    Stores a`Book` instance into ElasticSearch.
    :param Author book: A `Book` instance.
    """
    if not book.authors.count():
        logger.info(f"Book with id {book.id} has no authors. It can't be saved in ElasticSearch.")
        return

    es_client = ElasticSearchObject().get_client()

    try:
        es_client.index(
            index=current_app.config["ELASTIC_BOOKS_INDEX"],
            body=BookElasticSchema().dump(book),
            id=book.id,
        )
    except TransportError as exc:
        logger.error("Transport error. Invalid mapping.", exc)
