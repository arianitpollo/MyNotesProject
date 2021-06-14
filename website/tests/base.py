from unittest import  TestCase

from website import  db,create_app

from website.Models.models import User, Note


class BaseTestCase(TestCase):
    """A base test case."""


    def setUp(self):
        db.create_all(app=create_app())
        db.session.add(User("ad@min.com", "admin123", "admin"))
        db.session.add(
            Note("data for test note", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
