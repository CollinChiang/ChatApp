from FileWrite import FileWrite

from flask import Blueprint, request, render_template, redirect, session
from flask_socketio import Namespace
from utils.login_required import login_required

room_bp = Blueprint("room_bp", __name__, static_folder="static", template_folder="templates", static_url_path='/static')


class RoomNamespace(Namespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_message(self):
        pass


@room_bp.route("/")
@login_required
def list():
    pass


@room_bp.route("/private")
@login_required
def private_list():
    pass


@room_bp.route("/private/<int:room_id>")
@login_required
def join_private(room_id):
    pass


@room_bp.route("/server")
@login_required
def server_list():
    pass


@room_bp.route("/server/<int:server_id>")
@login_required
def join_server(server_id):
    pass


@room_bp.route("/server/<int:server_id>/<int:room_id>")
@login_required
def join_server_room(server_id, room_id):
    pass
