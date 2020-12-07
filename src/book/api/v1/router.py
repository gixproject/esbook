from book.api.v1.views import (
    books_api_v1,
    BookView,
    BooksView,
    BookAuthorsView,
    GenreBooksView,
)

books_api_v1.add_resource(BooksView, "", endpoint="books")
books_api_v1.add_resource(BookView, "<uuid:pk>/", endpoint="book_detail")
books_api_v1.add_resource(
    BookAuthorsView, "<uuid:pk>/authors/", endpoint="book_authors"
)
books_api_v1.add_resource(
    GenreBooksView, "genre/<string:name>/", endpoint="genre_books"
)
