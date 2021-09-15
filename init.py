from flask import Flask

from blueprints import register_blueprint
from core.enums import Environment
from configuration.config import config
from core.extensions import db, ma, migrate


def create_app(environment: Environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])
    db.init_app(app)
    ma.init_app(app)
    register_blueprint(app)
    migrate.init_app(app, db)
    # with app.app_context():
    #     db.create_all()
    return app
