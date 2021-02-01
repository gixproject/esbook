from author.api.views import authors_api_v1, AuthorBooksView

authors_api_v1.add_resource(
    AuthorBooksView, "<uuid:pk>/books/", endpoint="author_books"
)
