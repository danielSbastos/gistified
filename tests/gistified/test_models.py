from ..conf import ApplicationTestCase
from gistified.models import Gist
from gistified.lang_detection import which_lang
from gistified import db


class ModelsTest(ApplicationTestCase):

    def test_save_code_snippet(self):
        title = 'daniel.py'
        body = """
            def hahaha(num):
                return num*num
            """
        language = which_lang(title)

        gist = Gist(title, body, language)
        db.session.add(gist)
        db.session.commit()

        saved_gist = Gist.query.first()
        self.assertEqual(saved_gist.title, title)
        self.assertEqual(saved_gist.body, body)
        self.assertEqual(saved_gist.lang, language)
