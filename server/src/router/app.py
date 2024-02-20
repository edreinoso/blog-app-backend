from flask import Flask
from flask_cors import CORS
from src.data_access import init_db

from .blueprints.blogpost import blueprint_blogpost
from .blueprints.users import blueprint_users
from .middleware.auth import login_manager


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    app.debug = True
    app.config.from_pyfile(config_file)
    register_extensions(app)
    register_blueprints(app)
    init_db()
    return app


def register_extensions(app: Flask):
    CORS().init_app(app)
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(blueprint_users)
    app.register_blueprint(blueprint_blogpost)
