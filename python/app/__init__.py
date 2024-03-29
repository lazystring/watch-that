from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO

from config import app_config

socketio = SocketIO()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    if config_name is not 'testing':
        app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db)

    from app import models
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    socketio.init_app(app)

    return app
