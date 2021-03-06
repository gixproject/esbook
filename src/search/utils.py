import logging

from elasticsearch import Elasticsearch
from flask import current_app

from search.mapping import get_indexes

logger = logging.getLogger(__name__)


class ElasticSearch(Elasticsearch):
    def __init__(self, *args, **kwargs):
        """
        Overrides ElasticSearch instance initialize with correct URI.
        """
        kwargs.update(hosts=current_app.config["ELASTICSEARCH_URI"])
        super(ElasticSearch, self).__init__(*args, **kwargs)
        self.create_indexes()

    def create_indexes(self) -> None:
        """
        Creates indexes within Elasticsearch.
        """
        indexes = get_indexes()
        for index_name, index_body in indexes.items():
            try:
                if not self.indices.exists(index_name):
                    self.indices.create(index=index_name, body=index_body)
                    logger.info("Created Index for %s.", index_name)
            except Exception as ex:
                logger.error(ex)


def build_search_query(query, page, per_page) -> dict:
    """
    Build the multi-search query for Elasticsearch.
    :param str query:
    :param int page:
    :param int per_page:
    """
    search_query = {
        "query": {"multi_match": {"query": query, "fields": ["*"]}},
        "from": (page - 1) * per_page,
        "size": per_page,
    }

    return search_query


def get_search_hits(search_results) -> list:
    """
    Returns a list of `_source` results.
    :param dict search_results:
    """
    return [hit["_source"] for hit in search_results["hits"]["hits"]]


def get_paginated_response(search_results, page, per_page) -> dict:
    """
    Returns paginated response from ES.
    :param int page:
    :param int per_page:
    :param dict search_results:
    """
    count = search_results["hits"]["total"]["value"]
    results = get_search_hits(search_results)
    pages_count = max(1, count / per_page) if results else 0
    page = page if results else 0

    response = {
        "page": page,
        "pages_count": pages_count,
        "per_page": per_page,
        "count": count,
        "results": results,
    }

    return response
