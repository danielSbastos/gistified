from unittest import TestCase

from gistified.lang_detection import which_lang


class LangDetectionTest(TestCase):

    def test_detect_ruby(self):
        title = 'sherlock.rb'
        language = which_lang(title)

        self.assertEqual(language, 'Ruby')

    def test_detect_python(self):
        title = 'sherlock.py'
        language = which_lang(title)

        self.assertEqual(language, 'Python')

    def test_detect_cobol(self):
        title = 'sherlock.cob'
        language = which_lang(title)

        self.assertEqual(language, 'Cobol')

    def test_detect_c(self):
        title = 'sherlock.hpp'
        language = which_lang(title)

        self.assertEqual(language, 'Cpp')

    def test_detect_arduino(self):
        title = 'sherlock.ino'
        language = which_lang(title)

        self.assertEqual(language, 'Arduino')

    def test_detect_jons(self):
        title = 'sherlock.json'
        language = which_lang(title)

        self.assertEqual(language, 'Json')

    def test_detect_erlang(self):
        title = 'sherlock.erl'
        language = which_lang(title)

        self.assertEqual(language, 'Erlang')

    def test_detect_go(self):
        title = 'sherlock.go'
        language = which_lang(title)

        self.assertEqual(language, 'Go')

    def test_detect_javascript(self):
        title = 'sherlock.js'
        language = which_lang(title)

        self.assertEqual(language, 'Javascript')
