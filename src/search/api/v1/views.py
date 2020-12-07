from flask import jsonify, current_app
from flask_restplus import Namespace

from author.models import Author
from book.models import Book
from esbook.helpers import APIView
from search.helpers import search_request_parser
from search.services import es_search

search_api_v1 = Namespace("Search", ordered=True)


class SearchBooksView(APIView):
    @search_api_v1.expect(search_request_parser())
    def get(self):
        """
        Search among books.
        """
        search_args = search_request_parser().parse_args()
        search_results = es_search(
            index=current_app.config["ELASTIC_BOOKS_INDEX"],
            model=Book,
            **search_args,
        )

        return jsonify(search_results)


class SearchAuthorsView(APIView):
    @search_api_v1.expect(search_request_parser())
    def get(self):
        """
        Search among authors.
        """
        search_args = search_request_parser().parse_args()
        search_results = es_search(
            index=current_app.config["ELASTIC_AUTHORS_INDEX"],
            model=Author,
            **search_args,
        )

        return jsonify(search_results)
