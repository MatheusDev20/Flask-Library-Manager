from app.db import db

class BaseDbOperations():
    def __init__(self, model):
        self.model = model  

    def add(self, data):
        if not isinstance(data, dict):
            return

        db.session.add(self.model(**data))
        db.session.commit()
        db.session.close()

        db.session.rollback()
        db.session.close()

        db.session.close()