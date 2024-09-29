from src.models.base import db
from src.models.user import User
class FetchUsers:
    def __init__(self) -> None:
        self.db = db
    def execute(self):
        query = self.db.select(User)
        results = self.db.session.execute(query).scalars()
        return {"users": [{"id": result.id, "username": result.username, "role": result.role.name } for result in results]}