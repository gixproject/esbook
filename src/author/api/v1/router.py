from author.api.v1.views import authors_api_v1, AuthorBooksView

authors_api_v1.add_resource(AuthorBooksView, "<uuid:pk>/books/")
