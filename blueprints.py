from applications.admin_app.admin_app import admin_app
from applications.user_app.user_app import user_app


def register_blueprint(app):
    app.register_blueprint(admin_app, url_prefix="/admin")
    app.register_blueprint(user_app, url_prefix="")
