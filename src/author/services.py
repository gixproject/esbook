import logging

from elasticsearch.exceptions import TransportError
from flask import current_app

from author.schemes import AuthorElasticSchema
from search.services import ElasticSearchObject

logger = logging.getLogger(__name__)


def save_author_to_es(author) -> None:
    """
    Stores an `Author` instance into ElasticSearch.
    :param Author author: An `Author` instance.
    """
    es_client = ElasticSearchObject().get_client()

    try:
        es_client.index(
            index=current_app.config["ELASTIC_AUTHORS_INDEX"],
            body=AuthorElasticSchema().dump(author),
            id=author.id,
        )
    except TransportError as exc:
        logger.error("Transport error. Invalid mapping.", exc)
