import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()
api=Api()


def create_app(test_config=None, db=db):
    app = Flask(__name__, instance_relative_config=True)

    # DB config
    app.config.from_object(config)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'urlcutter.sqlite'),
    # )
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # allow CORS
    CORS(app)
    # rest-api
    api.init_app(app)
    # routes
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
