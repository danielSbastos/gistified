from ..conf import ApplicationTestCase
from gistified.models import Gist
from gistified.lang_detection import which_lang
from gistified import db


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
        self.assertTrue(b'Filename' in response.data)
        self.assertTrue(b'Gist' in response.data)

    def test_post_gists_create(self):
        title = 'test.py'
        body = 'print("Hello, World!")'

        response = self.client.post(
            '/gists/create',
            data=dict(title=title, body=body)
        )
        self.assertRedirects(response, '/gist/1')
        self.assertEqual(Gist.query.count(), 1)
        self.assertEqual(Gist.query.all()[0].title, title)
        self.assertEqual(Gist.query.all()[0].body, body)

    def test_show_individual_gist(self):
        title = 'test.py'
        body = 'print("Hello, World!")'
        lang = which_lang(title)

        self.__create_gist(title, body, lang)
        response = self.client.get('/gist/1')

        self.assert_template_used('gist_id.html')
        self.assertTrue(title in str(response.data))
        self.assertTrue(lang in str(response.data))

    def test_wrong_id_returns_404(self):
        response = self.client.get('/gist/bla')

        with self.assertRaises(Exception):
            self.assertEqual(response, 404)

    def test_all_gists(self):
        gists = [{
            'title': 'hello.py',
            'body': """
                    def add(a, b):
                        return a + b
                    """,
            'lang': 'Python'
            }, {
            'title': 'hello.rb',
            'body': """
                    def add(a, b)
                        a + b
                    end
                    """,
            'lang': 'Ruby'
        }]
        for gist in gists:
            self.__create_gist(gist['title'], gist['body'], gist['lang'])

        response = self.client.get('/gists')
        self.assert_template_used('gists.html')
        self.assertTrue(gists[0]['title'] in str(response.data))
        self.assertTrue('/gist/1' in str(response.data))
        self.assertTrue(gists[1]['title'] in str(response.data))
        self.assertTrue('/gist/2' in str(response.data))

    def test_delete_gist(self):
        self.__create_gist('test1.rb', "'1'.to_i", 'Ruby')
        self.__create_gist('test2.rb', "'2'.to_i", 'Ruby')

        response = self.client.post(
            f'/gist/1/delete',
        )

        deleted_gist = Gist.query.filter_by(title='test1.rb').first()
        all_gists = Gist.query.all()
        self.assertFalse(deleted_gist)
        self.assertEqual(len(all_gists), 1)
        self.assertEqual(all_gists[0].id, 2)

    @staticmethod
    def __create_gist(title, body, lang):
        gist = Gist(title=title, body=body, lang=lang)
        db.session.add(gist)
        db.session.commit()
