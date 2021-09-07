from datetime import datetime
from uuid import uuid4

from core.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
