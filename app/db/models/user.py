from app.db import db
from app.db.enums.role import Roles
from sqlalchemy.dialects.postgresql import ENUM as pgEnum

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    admin = db.Column(db.Boolean(), default=False, nullable=False)
    role = db.Column(pgEnum(Roles), unique=False, nullable=False, default='operation')
    avatar = db.Column(db.String(200), nullable=False)  

    def __repr__(self):
        return '<User %r>' % self.username