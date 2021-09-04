from FileWrite import FileWrite

from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, Namespace
from flask_session import Session
from config import ProductionConfig, DevelopmentConfig, TestingConfig
from functools import wraps

from auth.auth import auth_bp, AuthNamespace


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

Session(app)
db = SQLAlchemy(app)
socketio = SocketIO(app)

app.register_blueprint(auth_bp, url_prefix="/")


class RoomNamespace(Namespace):
    def on_connect(self):

        pass

    def on_disconnect(self):
        pass

    def on_message(self):
        pass


class DirectMessageNamespace(Namespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_message(self):
        pass


def login_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:  # TODO TEMPORARY
            return redirect("/login")
        return function(*args, **kwargs)
    return decorated_function


@app.route("/")
@login_required
def index():
    username = session.get("username")
    password = session.get("password")

    return render_template("index.html", username=username, password=password)


@socketio.on("connect")
def client_connect():
    print("Client connected!")


@socketio.on("disconnect")
def client_disconnect():
    print("Client disconnected!")


@socketio.on("message")
def handle_message(msg):
    print(f"Message: {msg}")
    socketio.send(msg, broadcast=True)


socketio.on_namespace(AuthNamespace("/auth"))
socketio.on_namespace(RoomNamespace("/chat-room"))
socketio.on_namespace(DirectMessageNamespace("/chat-direct"))

if __name__ == '__main__':
    FileWrite.clear()
    socketio.run(app, host="0.0.0.0")
