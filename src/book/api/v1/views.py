from flask_restplus import Namespace
from flask_restplus._http import HTTPStatus

from author.schemes import AuthorModelSchema
from book.models import Book, Genre
from book.schemes import BookModelSchema
from esbook.helpers import APIView, get_pagination_request_params

books_api_v1 = Namespace("Books", description="Books related operations.", ordered=True)


class BookView(APIView):

    @books_api_v1.doc(responses={
        HTTPStatus.NOT_FOUND: HTTPStatus.NOT_FOUND.phrase,
    })
    def get(self, pk):
        """
        Get a book object.
        """
        book = Book.query.get_or_404(pk)
        return BookModelSchema().dump(book)


class BookAuthorsView(APIView):

    @books_api_v1.doc(responses={
        HTTPStatus.NOT_FOUND: HTTPStatus.NOT_FOUND.phrase,
    })
    def get(self, pk):
        """
        Get a book authors.
        """
        book = Book.query.get_or_404(pk)
        paginated_queryset = self.paginate_queryset(book.authors.order_by("given_name"))
        serialized_data = AuthorModelSchema(many=True).dump(paginated_queryset)

        return self.get_paginated_response(serialized_data)


class GenreBooksView(APIView):

    @books_api_v1.doc(
        responses={
            HTTPStatus.NOT_FOUND: HTTPStatus.NOT_FOUND.phrase,
        },
        params=get_pagination_request_params(),
    )
    def get(self, name):
        """
        Get books by genre name.
        """
        genre = Genre.query.get_or_404(name.lower())
        paginated_queryset = self.paginate_queryset(genre.books.order_by("created_at"))
        serialized_data = BookModelSchema(many=True).dump(paginated_queryset)

        return self.get_paginated_response(serialized_data)


class BooksView(APIView):

    @books_api_v1.doc(
        params=get_pagination_request_params(),
    )
    @books_api_v1.deprecated
    def get(self):
        """
        Returns a list of books in a random order.
        """
        books = Book.query.all()
        paginated_queryset = self.paginate_queryset(books)
        serialized_data = BookModelSchema(many=True).dump(paginated_queryset)

        return self.get_paginated_response(serialized_data)
