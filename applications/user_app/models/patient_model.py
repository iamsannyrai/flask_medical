from applications.user_app.models.user_model import UserModel
from core.extensions import db


class PatientModel(UserModel):
    __tablename__ = "patients"
    role_id = db.Column(db.String, db.ForeignKey('roles.id'))
    role = db.relationship('RoleModel')
