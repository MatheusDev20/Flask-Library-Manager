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

    def get_by_email(self, email):
        if not email:
            return

        user_info = self.model.query.filter_by(email=email).first()

        if not user_info:
            return {
                "status": 404,
                "message": "User not found",
            }
    
        return {
            "status": 200,
            "message": "Success",
            "data": user_info
        }

    def get_all(self):
        all_users = self.model.query.all()
        return all_users

        