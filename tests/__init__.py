import unittest

from manage import app, db


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.app = app
        cls.client = cls.app.test_client()
        cls._ctx = cls.app.test_request_context()
        cls._ctx.push()
        db.init_app(cls.app)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        db.get_engine(cls.app).dispose()
        cls._ctx.pop()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
