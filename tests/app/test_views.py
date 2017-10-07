from ..conf import ApplicationTestCase
from app.models import Gist
from app import db


class TestViews(ApplicationTestCase):

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

        self.assertRedirects(response, '/gist/1')
        self.assertEqual(Gist.query.count(), 1)
        self.assertEqual(Gist.query.all()[0].title, 'test.py')
        self.assertEqual(Gist.query.all()[0].body, 'test.test')

    def test_show_individual_gist(self):
        self._create_gist('test.py', 'test.test')
        response = self.client.get('/gist/1')

        self.assert_template_used('gist_id.html')
        self.assertTrue(b'test.py' in response.data)
        self.assertTrue(b'test.test' in response.data)

    @staticmethod
    def _create_gist(title, body):
        gist = Gist(title=title, body=body)
        db.session.add(gist)
        db.session.commit()
