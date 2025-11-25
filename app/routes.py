from flask import Blueprint, request, jsonify
from .controllers import get_all_users, create_user

bp = Blueprint("main", __name__)

@bp.route("/users", methods=["GET"])
def list_users():
    users = get_all_users()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@bp.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user = create_user(data["name"])
    return jsonify({"id": user.id, "name": user.name}), 201

