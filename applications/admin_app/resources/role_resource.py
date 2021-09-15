from flask import request
from flask_restful import Resource

from applications.admin_app.managers.admin_app_manager import AdminAppManager
from applications.admin_app.schemas.role_schema import RoleSchema


class RoleResource(Resource):

    def __init__(self):
        self.role_schema = RoleSchema()
        self.role_schemas = RoleSchema(many=True)

    def get(self, role_id=None):
        if role_id:
            role = AdminAppManager.get_role(role_id)
            return self.role_schema.dump(role)
        else:
            roles = AdminAppManager.get_roles()
            return self.role_schemas.dump(roles)

    def post(self):
        role_dict = request.get_json()
        role = AdminAppManager.create_role(role_dict['role'])
        return self.role_schema.dump(role), 201

    @staticmethod
    def delete(role_id):
        AdminAppManager.delete_role(role_id)
        return {}, 204
