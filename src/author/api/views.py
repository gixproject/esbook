from flask_restplus import Namespace
from flask_restplus._http import HTTPStatus

from author.models import Author
from book.schemes import BookModelSchema
from esbook.helpers import get_pagination_request_params, APIView

authors_api_v1 = Namespace(
    "Authors", description="Authors related operations.", ordered=True
)


class AuthorBooksView(APIView):
    @authors_api_v1.doc(
        responses={
            HTTPStatus.NOT_FOUND: HTTPStatus.NOT_FOUND.phrase,
        },
        params=get_pagination_request_params(),
    )
    def get(self, pk):
        """
        Get an author books.
        """
        author = Author.query.get_or_404(pk)
        paginated_queryset = self.paginate_queryset(author.books.order_by("created_at"))
        serialized_data = BookModelSchema(many=True).dump(paginated_queryset)

        return self.get_paginated_response(serialized_data)
