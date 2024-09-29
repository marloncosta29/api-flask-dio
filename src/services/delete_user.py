from src.models.base import db
from src.models.user import User

class DeleteUser:
    def execute(self, user_id):
        user = db.get_or_404(User, user_id)
        db.session.delete(user)
        db.session.commit()
        return ""