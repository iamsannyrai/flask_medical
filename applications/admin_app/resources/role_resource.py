from flask import request
from flask_restful import Resource

from applications.admin_app.managers.admin_app_manager import AdminAppManager
from applications.admin_app.schemas.role_schema import RoleSchema


class RoleResource(Resource):

    def __init__(self):
        self.admin_app_manager = AdminAppManager()
        self.role_schema = RoleSchema()
        self.role_schemas = RoleSchema(many=True)

    def get(self, role_id=None):
        if role_id:
            role = self.admin_app_manager.get_role(role_id)
            return self.role_schema.dump(role)
        else:
            roles = self.admin_app_manager.get_roles()
            return self.role_schemas.dump(roles)

    def post(self):
        role_dict = request.get_json()
        role = self.admin_app_manager.create_role(role_dict['role'])
        return self.role_schema.dump(role), 201

    def delete(self, role_id):
        self.admin_app_manager.delete_role(role_id)
        return {}, 204
