from app.db import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(200), nullable=False)  
    description = db.Column(db.String(240), nullable=True)
    author = db.Column(db.String(160), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title