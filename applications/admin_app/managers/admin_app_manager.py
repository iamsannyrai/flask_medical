from applications.user_app.models.role_model import RoleModel
from core.extensions import db


class AdminAppManager:
    def get_role(self, role_id):
        role = RoleModel.query.get(role_id)
        return role

    def get_roles(self):
        roles = RoleModel.query.all()
        return roles

    def create_role(self, role):
        role_model = RoleModel(role=role)
        db.session.add(role_model)
        db.session.commit()
        return role_model

    def delete_role(self, role_id):
        role = RoleModel.query.get(role_id)
        db.session.delete(role)
        db.session.commit()
