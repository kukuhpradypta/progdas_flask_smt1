import os

from flask import Flask
from flask_bootstrap import Bootstrap


def root_dir():  # pragma: no covery
    return os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "indRlaHR4dVSIOFO4w7I4LScz0FBzxCR"

    Bootstrap(app)

    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.list import list as list_blueprint
    app.register_blueprint(list_blueprint)

    return app
