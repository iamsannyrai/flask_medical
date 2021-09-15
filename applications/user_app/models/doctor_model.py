from core.extensions import db
from applications.user_app.models.user_model import UserModel


class DoctorModel(UserModel):
    __tablename__ = "doctors"
    nmc_number = db.Column(db.String)
    role_id = db.Column(db.String, db.ForeignKey('roles.id'))
    role = db.relationship('RoleModel')
