from applications.user_app.models.role_model import RoleModel
from core.extensions import db


class AdminAppManager:
    @staticmethod
    def get_role(role_id):
        role = RoleModel.query.get(role_id)
        return role

    @staticmethod
    def get_roles():
        roles = RoleModel.query.all()
        return roles

    @staticmethod
    def create_role(role):
        role_model = RoleModel(role=role)
        db.session.add(role_model)
        db.session.commit()
        return role_model

    @staticmethod
    def delete_role(role_id):
        role = RoleModel.query.get(role_id)
        db.session.delete(role)
        db.session.commit()
