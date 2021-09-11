from applications.common.models.base_model import BaseModel
from core.extensions import db


class UserModel(BaseModel):
    __abstract__ = True
    full_name = db.Column(db.String(30))
    dob = db.Column(db.Date)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String(30))
    phone_number = db.Column(db.String(10))
    blood_group = db.Column(db.String)
    password = db.Column(db.String)
