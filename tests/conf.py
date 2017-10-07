import os

from flask_testing import TestCase

from app import create_app, db


class ApplicationTestCase(TestCase):

    def create_app(self):
        app = create_app()
        if os.getenv('CIRCLECI'):
            database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
        else:
            database_uri = 'postgresql:///gistified_test'

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
        db.init_app(app)
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
