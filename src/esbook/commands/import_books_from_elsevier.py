import logging

import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from flask_script import Command, Option

from author.models import Author
from book.models import Book
from book.services import save_book_to_es
from esbook.utils import split_name_from_full_name

logger = logging.getLogger(__name__)

ELSEVIER_CATALOG_URL = "https://www.elsevier.com/catalog?producttype=books"


class ElsevierScraper(Command):
    """
    This is the sample scraper for https://elsevier.com/.
    """

    option_list = (
        Option("--offset", dest="offset", default=0, type=int, help="Page offset"),
        Option(
            "--sort",
            dest="sort",
            default="dateasc",
            type=str,
            choices=("dateasc", "datedesc"),
            help="Sort by date",
        ),
        Option("--size", dest="size", default=20, type=int, help="Page size"),
    )

    def run(self, offset, sort, size):
        """
        It's just an example of scraper using BeautifulSoup.
        However, it has it's own Python SDK. https://dev.elsevier.com/.
        Please, use an API for real projects.
        """
        page_number = offset

        while True:
            page = requests.get(
                f"{ELSEVIER_CATALOG_URL}&page={page_number}&sort={sort}&size={size}"
            )
            page_text = BeautifulSoup(page.text, "html.parser")
            book_urls_tags = page_text.find_all(
                attrs={"class": "cta-primary view-product-link exit-link"}
            )

            for book_url_tag in book_urls_tags:
                book_url = book_url_tag.get("href")

                try:
                    book_details = self.parse_book_details(url=book_url)
                except Exception as exc:
                    logger.exception(f"{exc}. {book_url}")
                    continue

                # Skip if book exists
                if Book.query.filter_by(isbn=book_details["general"]["isbn"]).first():
                    continue

                book = Book(**book_details["general"])

                for author in book_details["authors"]:
                    names_dict = split_name_from_full_name(author)
                    author = Author(**names_dict)
                    book.authors.append(author)

                try:
                    book.save()
                    save_book_to_es(book)
                except Exception as exc:
                    logger.exception(f"{exc}. {book_url}")
                    continue

                logger.info(
                    'Book "{}" was processed on page {}.'.format(
                        book_details["general"]["title"], page_number
                    )
                )
            page_number += 1

    @staticmethod
    def parse_book_details(url) -> dict:
        """
        Parses book info into a suitable format.
        :param url: A book URL in a catalogue.
        """
        response = requests.get(url)
        book_details = BeautifulSoup(response.text, "html.parser")

        weaks = book_details.find_all(attrs={"class": "weak inline"})
        weaks_list = []
        for weak in weaks:
            weaks_list.append(weak.text.strip().split(": "))
        weaks_dict = dict(weaks_list)

        # Prepare general info
        title = book_details.select_one(".main-title.book-title").text.strip()
        subtitle = book_details.select_one(".weak.subtitle")
        publication_date = parse(weaks_dict["Published Date"])
        description_section = book_details.select_one("#description")
        description = description_section.div.p.text if description_section else ""
        price_section = book_details.select_one(".price-value")
        price = float(price_section.text.strip()) if price_section else None
        language = book_details.select_one(".inLanguage.language").text.strip()
        isbn_section = book_details.select_one(".weak.inline.eman")
        isbn = isbn_section.text.split(":")[1].strip() if isbn_section else None

        general = {
            "title": title,
            "description": description,
            "publisher": weaks_dict["Imprint"],
            "publication_date": publication_date,
            "pages": int(weaks_dict["Page Count"]),
            "subtitle": subtitle.text if subtitle else "",
            "price": price,
            "isbn": isbn,
            "copyright": weaks_dict["Imprint"],
            "language": language,
            "url": url,
            "source": "Elsevier",
        }

        # Prepare valid authors names
        authors = book_details.find_all(attrs={"class": "inline weak editor"})
        authors_list = []
        for author in authors:
            authors_list.append(author.text.strip())

        return {"general": general, "authors": authors_list}
