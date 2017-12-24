from . import db


class Gist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    lang = db.Column(db.String(30))

    def __init__(self, title, body, lang):
        self.title = title
        self.body = body
        self.lang = lang

    def __repr__(self):
        return self.title

    @staticmethod
    def is_lang_defined(gist):
        return gist.lang != "Undefined"
