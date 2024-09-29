from flask_sqlalchemy import SQLAlchemy

from src.models.user import User
from src.models.base import db
class CreateUser:
    def create_user(self, data):
        user = User()
        user.username = data["username"]
        user.password = data["password"]
        user.role_id = data["role_id"]

        db.session.add(user)
        db.session.commit()
        return  { "user_id":  user.id }