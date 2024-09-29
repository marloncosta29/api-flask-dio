from flask import Blueprint, request
from ..models import Role, db
from http import HTTPStatus

from flask_jwt_extended import create_access_token


app = Blueprint("role", __name__, url_prefix="/role")

@app.route("/", methods=["GET", "POST"])
def create():
    data = request.json
    role = Role()
    role.name = data['name']
    db.session.add(role)
    db.session.commit()
    return {'message': "Role created"}, HTTPStatus.CREATED



