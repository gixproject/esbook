from book.api.v1.views import books_api_v1, BookView, BooksView, BookAuthorsView, GenreBooksView

books_api_v1.add_resource(BooksView, "")
books_api_v1.add_resource(BookView, "<uuid:pk>/")
books_api_v1.add_resource(BookAuthorsView, "<uuid:pk>/authors/")
books_api_v1.add_resource(GenreBooksView, "genre/<string:name>/")
