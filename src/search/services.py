import logging

from sqlalchemy.orm.exc import NoResultFound

from author.models import Author
from author.schemes import AuthorModelSchema
from book.models import Book
from book.schemes import BookModelSchema
from search.utils import ElasticSearch, build_search_query, get_paginated_response

logger = logging.getLogger(__name__)


def es_search(index, model, query, page, per_page) -> dict:
    """
    Search among index.
    Returns paginated results.
    :param str index: ElasticSearch index name.
    :param object model: SQLAlchemy model.
    :param str query: Search query.
    :param int page:
    :param int per_page:
    """
    es_client = ElasticSearch()

    schemas = {
        Book: BookModelSchema(),
        Author: AuthorModelSchema(),
    }

    search_results = es_client.search(
        index=index, body=build_search_query(query=query, page=page, per_page=per_page)
    )
    paginated_results = get_paginated_response(
        search_results=search_results, page=page, per_page=per_page
    )
    results = []

    for result in paginated_results["results"]:
        try:
            entity = model.query.get(result["source_id"])
            results.append(schemas[model].dump(obj=entity))
        except NoResultFound as exc:
            logger.warning(exc)
            pass

    paginated_results["results"] = results

    return paginated_results
