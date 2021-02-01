from flask import current_app


def get_indexes():
    """
    Get Elasticsearch indexes mapping.
    """
    config = current_app.config

    indexes = {
        config["ELASTIC_BOOKS_INDEX"]: {
            "settings": {
                "number_of_shards": 4,
                "number_of_replicas": 2,
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "source_id": {
                        "type": "text",
                    },
                    "title": {
                        "type": "text",
                        "fielddata": True,
                    },
                    "updated_at": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss",
                    },
                    "publication_date": {
                        "type": "date",
                        "format": "yyyy-MM-dd",
                    },
                    "issn": {
                        "type": "text",
                    },
                    "isbn": {
                        "type": "text",
                    },
                    "publisher": {
                        "type": "text",
                        "fielddata": True,
                    },
                    "subtitle": {
                        "type": "text",
                    },
                    "description": {
                        "type": "text",
                    },
                    "genres": {
                        "type": "text",
                    },
                    "authors": {
                        "type": "text",
                    },
                    "pages": {
                        "type": "integer",
                    },
                },
            },
        },
        config["ELASTIC_AUTHORS_INDEX"]: {
            "settings": {
                "number_of_shards": 4,
                "number_of_replicas": 2,
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "source_id": {
                        "type": "text",
                    },
                    "updated_at": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss",
                    },
                    "given_name": {
                        "type": "text",
                        "fielddata": True,
                    },
                    "family_name": {
                        "type": "text",
                        "fielddata": True,
                    },
                    "middle_name": {
                        "type": "text",
                        "fielddata": True,
                    },
                },
            },
        },
    }

    return indexes
