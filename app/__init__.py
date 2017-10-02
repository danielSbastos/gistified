import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gistified'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models
    from app import views

    return app
