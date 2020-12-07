from flask_restplus.reqparse import RequestParser


def search_request_parser() -> RequestParser:
    """
    Request parser for search APIs.
    """
    search_parser = RequestParser()
    search_parser.add_argument(
        "query", type=str, help="Search query", required=True
    )
    search_parser.add_argument("page", type=int, help="Page", default=1)
    search_parser.add_argument(
        "per_page", type=int, help="Results per page", default=10
    )

    return search_parser
