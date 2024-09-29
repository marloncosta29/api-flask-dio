from sqlalchemy import inspect    

from src.models.base import db
from src.models.user import User

class PatchUser:
    def execute(self, user_id, data):
        user = db.get_or_404(User, user_id)
        mapper = inspect(User)
        for column in mapper.attrs:
            if column.key in data:
                setattr(user, column.key, data[column.key])

        db.session.commit()
        return { 
                "id" : user.id, 
                "username": user.username, 
                "role_id": user.role_id,
            }