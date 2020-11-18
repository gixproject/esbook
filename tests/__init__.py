import unittest

from manage import app, db
from config import config


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.app = app
        cls.app.config.from_object(config["testing"])
        cls.client = cls.app.test_client()
        cls.app.app_context().push()
        db.init_app(cls.app)
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        super().tearDownClass()
