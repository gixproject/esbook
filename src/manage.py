import os

from flask import Flask
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_restplus import Api
from flask_script import Manager

from author.api.v1.router import authors_api_v1
from book.api.v1.router import books_api_v1
from config import config
from db import db
from esbook.commands.helpers import ShowUrls, DatabaseRecreate
from esbook.commands.migrate_books_to_es import MigrateBooks
from esbook.commands.test_data import TestData
from search.api.v1.router import search_api_v1

app = Flask(__name__)

environment = os.environ.get("FLASK_ENV", "development")
app.config.from_object(config[environment])

db.init_app(app)
Migrate(app, db)

api = Api(
    app=app,
    doc="/",
    title="ESbook API",
    version="0.2",
    contact_url="https://github.com/gixproject",
    contact="gixproject",
    license_url="https://github.com/gixproject/esbook/blob/develop/LICENSE",
    license="Apache 2.0",
    ordered=True,
    description="The REST API platform that provides search within millions of books. "
    "The functionality allows you to retrieve data for a period or just by one author.",
)

app.config.from_object(config[os.environ["FLASK_ENV"]])  # FLASK_ENV must be set
db.init_app(app)
manager = Manager(app)
Migrate(app, db)

# Register namespaces
api.add_namespace(books_api_v1, path="/v1/books/")
api.add_namespace(authors_api_v1, path="/v1/authors/")
api.add_namespace(search_api_v1, path="/v1/search/")

# Register commands
manager.add_command("db", MigrateCommand)
manager.add_command("apply_test_data", TestData())
manager.add_command("migrate_books_to_es", MigrateBooks())
manager.add_command("show_urls", ShowUrls())
manager.add_command("reset_db", DatabaseRecreate())

if __name__ == "__main__":
    manager.run()
