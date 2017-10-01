import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import unittest

from app import create_app, db
from app.models import Gist
from flask_testing import TestCase


class TestViews(TestCase):

    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gistified_test'
        db.init_app(app)
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('home.html')
        self.assertTrue(b'View all gists' in response.data)
        self.assertTrue(b'Create new gist' in response.data)

    def test_get_gists_create(self):
        response = self.client.get('/gists/create')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('gists_create.html')
        self.assertTrue(b'Title' in response.data)
        self.assertTrue(b'Gist' in response.data)

    def test_post_gists_create(self):
        response = self.client.post('/gists/create', data=dict(
            title='test.py',
            body='test.test'
            )
        )
        self.assertRedirects(response, '/gists/create')
        self.assertEqual(Gist.query.count(), 1)
        self.assertEqual(Gist.query.all()[0].title, 'test.py')
        self.assertEqual(Gist.query.all()[0].body, 'test.test')
