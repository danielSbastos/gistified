from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from unittest import TestCase


class TestViews(TestCase):

    def setUp(self):
        # TODO: Import create_app from app __init__ instead of rewriting
        app = Flask(__name__, instance_relative_config=True)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gistified'
        app.config['TESTING'] = True

        db = SQLAlchemy()
        db.init_app(app)

        migrate = Migrate(app, db)

        self.app = app.test_client()

    def test_root_endpoint(self):
        response = self.app.get('/')
        self.assertTrue(response, 'Hello, World!')
