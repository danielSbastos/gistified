import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gistified'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

def create_app():
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models
    from app import views

    return app
