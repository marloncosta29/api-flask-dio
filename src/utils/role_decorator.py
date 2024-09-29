from functools import wraps
from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity
from src.models import User, db


def requires_role(role_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = db.get_or_404(User, user_id)

            if user.role.name != 'admin':
                return { "message": "User dont have access." }, HTTPStatus.FORBIDDEN 
            return f(*args, **kwargs)
        return wrapper
    return decorator