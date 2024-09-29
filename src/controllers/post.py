from flask import Blueprint, request
from ..models import Post, User, db
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.utils.role_decorator import requires_role

app = Blueprint("post", __name__, url_prefix="/posts")

@app.route("/", methods=["POST"])
@jwt_required()
@requires_role("admin")
def create():
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    data = request.json
    post = Post()
    post.author_id = user.id
    post.body = data["body"]
    post.title = data["title"]

    db.session.add(post)
    db.session.commit()
    return {'post_id': post.id }, HTTPStatus.CREATED



