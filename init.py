from flask import Flask

from core.enums import Environment
from configuration.config import config


def create_app(environment: Environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])
    return app
