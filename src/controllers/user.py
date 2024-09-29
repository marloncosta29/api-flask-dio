from flask import Blueprint, request
from ..models import User, db
from http import HTTPStatus

from src.services.create_user import CreateUser
from src.services.fetch_users import FetchUsers
from src.services.get_user_by_id import GetUserById
from src.services.patch_user import PatchUser
from src.services.delete_user import DeleteUser
from flask_jwt_extended import jwt_required

app = Blueprint("user", __name__, url_prefix="/users")

@app.route("/", methods=["POST"])
def handle_create_user():
    return CreateUser().create_user(request.json), HTTPStatus.CREATED

@app.route("/", methods=["GET"])
@jwt_required()
def handle_user():
   return FetchUsers().execute()

@app.route("/<int:user_id>")
@jwt_required()
def get_user_by_id(user_id):
    return GetUserById().execute(user_id)

@app.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
def update_user(user_id):
    return PatchUser().execute(user_id, data=request.json)

@app.route("/<int:user_id>",  methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    return DeleteUser().execute(user_id), HTTPStatus.NO_CONTENT
