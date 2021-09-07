from applications.admin_app.admin_app import admin_app


def register_blueprint(app):
    app.register_blueprint(admin_app, url_prefix="/admin")
