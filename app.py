from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, Namespace
from flask_session import Session
from config import ProductionConfig, DevelopmentConfig, TestingConfig
from functools import wraps

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

Session(app)
db = SQLAlchemy(app)
socketio = SocketIO(app)


class AuthorizationNamespace(Namespace):
    @staticmethod
    def on_connect():
        print("[AUTH] Client connected.")

    @staticmethod
    def on_disconnect():
        print("[AUTH] Client disconnected.")

    @staticmethod
    def on_authenticate(data):
        print("[AUTH] Client authenticated.")
        print(f"[AUTH] {data}")


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        session["username"] = username
        session["password"] = password

        return redirect("/")


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


socketio.on_namespace(AuthorizationNamespace("/auth"))
socketio.on_namespace(RoomNamespace("/chat-room"))
socketio.on_namespace(DirectMessageNamespace("/chat-direct"))

if __name__ == '__main__':
    socketio.run(app, debug=True)
