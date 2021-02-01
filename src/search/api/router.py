from search.api.views import search_api_v1, SearchBooksView, SearchAuthorsView

search_api_v1.add_resource(SearchBooksView, "books", endpoint="search_books")
search_api_v1.add_resource(SearchAuthorsView, "authors", endpoint="search_authors")
