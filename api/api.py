from flask import Blueprint

api_bp = Blueprint("api_bp", __name__)

@api_bp.route("/users", methods=["POST"])
def users():
    return "<List of Users>"
