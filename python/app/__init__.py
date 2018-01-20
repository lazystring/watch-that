from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config
from .views import app as app_blueprint

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    # Load config from instance/config.py if it exists.
    app.config.from_pyfile('config.py')
    db.init_app(app)

    app.register_blueprint(app_blueprint)

    return app
