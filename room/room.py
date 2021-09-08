from flask import Blueprint, render_template, session
from flask_socketio import Namespace

from database.models import db, User, Channel, Server

from utils.login_required import login_required
import json

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
    server_names = get_server_names()
    channel_names = get_channel_names()

    return render_template("room/room_list.html", server_names=server_names, channel_names=channel_names)



@room_bp.route("/add_channel")
@login_required
def add_channel():
    pass


@room_bp.route("/add_server")
@login_required
def add_server():
    pass


@room_bp.route("/channel")
@login_required
def channel_list():
    pass


@room_bp.route("/channel/<int:channel_id>")
@login_required
def join_channel(channel_id: int):
    pass


@room_bp.route("/private/<int:channel_id>/remove")
@login_required
def remove_channel(channel_id: int):
    pass


@room_bp.route("/server")
@login_required
def server_list():
    pass


@room_bp.route("/server/<int:server_id>")
@login_required
def join_server(server_id: int):
    pass


@room_bp.route("/server/<int:server_id>/remove")
@login_required
def remove_server(server_id: int):
    pass


@room_bp.route("/server/<int:server_id>/<int:channel_id>")
@login_required
def join_server_channel(server_id: int, channel_id: int):
    pass


@room_bp.route("/server/<int:server_id>/<int:channel_id>/remove")
@login_required
def remove_server_channel(server_id: int, channel_id: int):
    pass


def get_channel_ids():
    user = User.query.filter_by(id=session["user_id"]).first()
    channel_ids = json.loads(user.channel_ids)
    return channel_ids


def get_channel_names():
    channel_ids = get_channel_ids()
    channel_names = []

    for channel_id in channel_ids:
        channel = Channel.query.filter_by(id=channel_id, is_server=False).first()
        channel_names.append(channel.name)

    return channel_names


def get_server_ids():
    user = User.query.filter_by(id=session["user_id"]).first()
    server_ids = json.loads(user.server_ids)
    return server_ids


def get_server_names():
    server_ids = get_server_ids()
    server_names = []

    for server_id in server_ids:
        server = Server.query.filter_by(id=server_id).first()
        server_names.append(server.name)

    return server_names
