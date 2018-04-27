import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import
    Migrate


app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql:///gistified')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def create_app():
    db.init_app(app)
    migrate = Migrate(app, db)
    from gistified import models
    from gistified import views

    return app
