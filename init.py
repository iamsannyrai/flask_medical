from flask import Flask

from core.enums import Environment
from configuration.config import config
from core.extensions import db


def create_app(environment: Environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])
    db.init_app(app)
    return app
