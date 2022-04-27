from app.db import db
from app.db.enums.role import Roles
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    admin = db.Column(db.Boolean(), default=False, nullable=False)
    role = db.Column(pgEnum(Roles), unique=False, nullable=False, default='operation')
    avatar = db.Column(db.String(200), nullable=False)
    user_uuid = db.Column(UUID(as_uuid=True), nullable=False)
    extra_info = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username