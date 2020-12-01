from search.api.v1.views import search_api_v1, SearchBooksView, SearchAuthorsView

search_api_v1.add_resource(SearchBooksView, "books")
search_api_v1.add_resource(SearchAuthorsView, "authors")
