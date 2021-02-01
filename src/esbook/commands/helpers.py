from flask import current_app
from flask_script import Command

from db import db


class ShowUrls(Command):
    """
    Shows all current routes and their endpoint names.
    """

    def run(self):
        urls = []
        for rule in current_app.url_map.iter_rules():
            urls.append("{:50s} {:25s}".format(rule.rule, rule.endpoint))

        return "\n".join(urls)


class DatabaseRecreate(Command):
    """
    Deletes database tables and creates again.
    """

    def run(self):
        """
        Use only for development purposes.
        """
        db.session.remove()
        db.drop_all()
        db.create_all()
        db.session.commit()
