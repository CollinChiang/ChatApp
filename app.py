# flask libraries
from flask import Flask, request, render_template, redirect, session
from flask_socketio import SocketIO, Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from config import ProductionConfig, DevelopmentConfig, TestingConfig

# blueprints / namespaces
from api.api import api_bp
from auth.auth import auth_bp, AuthNamespace
from room.room import room_bp, RoomNamespace

# database
from database.models import db

# util methods
from utils.file_write import FileWrite
from utils.login_required import login_required

# flask configuration
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# flask-session / flask-socketio configuration
Session(app)
socketio = SocketIO(app)
db.init_app(app)

# blueprint registration
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/")
app.register_blueprint(room_bp, url_prefix="/room")


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
socketio.on_namespace(RoomNamespace("/room"))

if __name__ == '__main__':
    FileWrite.clear()
    socketio.run(app, host="0.0.0.0")
