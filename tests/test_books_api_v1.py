from flask import url_for

from tests import TestCase
from tests.factories import BookFactory, AuthorFactory, GenreFactory


class BookDetailTest(TestCase):

    def setUp(self):
        super(BookDetailTest, self).setUp()
        self.book = BookFactory(
            title="Python Tricks", subtitle="A Buffet of Awesome Python Features",
            publication_date="2017-10-25", language="English", description="...",
            isbn="isbn", pages=301, price=29.99, publisher="Dan Bader", issn=None,
            url="https://dbader.org/", source=None, doi=None, copyright="Dan Bader",
        )
        author = AuthorFactory(given_name="Dan", family_name="Bader")
        genre = GenreFactory()
        self.book.authors.append(author)
        self.book.genres.append(genre)
        self.book.save()

    def _get_url(self, pk=None):
        book_pk = pk or self.book.id
        return url_for("book_detail", pk=str(book_pk))

    def test_book_detail(self):
        expected_data = {
            "language": "English",
            "publisher": "Dan Bader",
            "publication_date": "2017-10-25",
            "authors": ["Dan Bader"],
            "id": str(self.book.id),
            "subtitle": "A Buffet of Awesome Python Features",
            "copyright": "Dan Bader",
            "title": "Python Tricks",
            "issn": None,
            "isbn": "isbn",
            "price": 29.99,
            "created_at": self.book.created_at.isoformat().replace("+00:00", "Z"),
            "genres": ["technical"],
            "description": "...",
            "pages": 301,
            "url": "https://dbader.org/",
            "source": None,
            "doi": None,
        }

        response = self.client.get(self._get_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), expected_data)

    def test_book_detail_with_non_existing_book(self):
        response = self.client.get(self._get_url("invalid_id"))
        self.assertEqual(response.status_code, 404)
