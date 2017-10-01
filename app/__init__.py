from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def root():
        return 'Hello, World!'

    migrate = Migrate(app, db)

    from app import models

    return app
