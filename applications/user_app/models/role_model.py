from applications.common.models.base_model import BaseModel
from core.extensions import db


class RoleModel(BaseModel):
    __tablename__ = "roles"
    role = db.Column(db.String(15), nullable=False)
