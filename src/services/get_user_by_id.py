from src.models.base import db
from src.models.user import User

class GetUserById:
    def __init__(self) -> None:
        self.db = db
    def execute(self, user_id):
        user = self.db.get_or_404(User, user_id)
        return { 
            "id" : user.id, 
            "username": user.username, 
            "role": user.role.name,
        }