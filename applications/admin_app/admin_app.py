from flask import Blueprint
from flask_restful import Api

from applications.admin_app.resources.role_resource import RoleResource

admin_app = Blueprint('admin_app', __name__)
api = Api(admin_app)

api.add_resource(RoleResource, "/roles", "/roles/<role_id>")
